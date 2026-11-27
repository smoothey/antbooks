// Builds the full Word review copy: full-page cover, title page, contents,
// parts, chapters with figures, glossary and notes.
const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, Footer,
        PageNumber, HeadingLevel, Bookmark, InternalHyperlink, SectionType,
        TabStopType, TabStopPosition } = require('docx');

const ROOT = '/home/claude/antbooks/books/build-the-thing/';
const CH = ROOT + 'chapters/', FIG = ROOT + 'figures/';
const DATE = '24 November 2026';
const SERIF = 'Georgia', SANS = 'Arial';
const ORANGE = 'C8701F', GREY = '777777';

// 6 x 9 inch trim, like the paperback
const PAGE = { width: 8640, height: 12960 };
const MARGIN = { top: 1152, bottom: 1152, left: 1080, right: 1080 };
const TEXT_W_PX = Math.round((PAGE.width - MARGIN.left - MARGIN.right) / 1440 * 96); // 432

// Written chapters, in book order
const written = ['00-introduction.md', '01-doing-the-work.md', '02-build-the-thing.md',
  '03-incremental-against-compound.md', '04-one-place-for-the-truth.md', '05-work-while-you-sleep.md',
  '06-a-night-in-the-life.md', '07-only-real-asks-reach-you.md', '08-rings-and-brokers.md',
  '13-the-echo-chamber.md'];

// Figures: after the paragraph with this id (or matching text), with a caption
const figures = {
  '02': [{ after: t => t.startsWith('The site grew quickly'), file: 'fig02a-admin-grew.png', cap: "Charlie's admin area on 13, 16 and 25 October, as it grew." },
         { after: t => t.startsWith('None of this was designed up front'), file: 'fig02b-how-it-grew.png', cap: 'One problem at a time: how the system grew.' }],
  '03': [{ after: 3, file: 'fig03a-incremental-vs-compound.png', cap: 'Incremental is capped. Compound keeps climbing.' },
         { after: 10, file: 'fig03c-share-of-a-night.png', cap: 'Sizing work as a share of a night.' },
         { after: 14, file: 'fig03b-changes-per-week.png', cap: 'Changes saved per week across six projects.' }],
  '04': [{ markerAfter: true, file: 'fig04-one-truth-three-doors.png', cap: 'One place for the truth, with three front doors.' }],
  '05': [{ markerAfter: true, file: 'fig05a-minutes-per-night.png', cap: 'Minutes used per night, out of 480.' }],
  '06': [{ markerAfter: true, file: 'fig06-a-night-hour-by-hour.png', cap: 'The night of 18 November, hour by hour.' }],
  '07': [{ after: 8, file: 'fig07-needs-you.png', cap: 'The Needs you list (an illustration in the style of the real one).' }],
  '08': [{ after: 2, file: 'fig08-privacy-rings.png', cap: 'The privacy rings.' }],
};

// The whole plan, for the contents page
const plan = [
  { part: null, items: [['Introduction', '00']] },
  { part: 'Part 1: The shift', items: [['1. Doing the work, and the ceiling it hits', '01'], ['2. Build the thing that builds the things', '02'], ['3. Incremental against compound', '03']] },
  { part: 'Part 2: The machine', items: [['4. One place for the truth', '04'], ['5. Work while you sleep', '05'], ['6. A night in the life', '06'], ['7. Only real asks reach you', '07'], ['8. Rings and brokers', '08'], ['9. The people around you', null]] },
  { part: 'Part 3: What it teaches you', items: [['10. Logging a lesson isn\u2019t learning it', null], ['11. Best practice by accident', null], ['12. Driving, or being driven?', null], ['13. The echo chamber', '13'], ['14. When the machine says no', null], ['15. What experience knows that nobody writes down', null], ['16. Risk, measure and boldness', null], ['17. Working with AI is still work', null], ['18. Learning by building', null], ['19. What it costs', null]] },
  { part: 'Part 4: Your turn', items: [['20. Start small: one loop, one record, one rule', null], ['21. Ways of working with AI', null], ['22. Many projects from one hub', null], ['23. A production line, end to end', null], ['24. The right tool for each job', null], ['25. What comes next', null]] },
  { part: 'At the back', items: [['Closing chapter', null], ['Appendix: starter kit', null], ['Glossary', 'gloss'], ['Notes and further reading', 'notes'], ['Acknowledgements', null], ['How this book was made', null]] },
];
const partBefore = { '01': 'Part 1: The shift', '04': 'Part 2: The machine', '13': 'Part 3: What it teaches you' };

function smart(t) {
  t = t.replace(/(^|[\s(\[—–-])"/g, '$1\u201C').replace(/"/g, '\u201D');
  t = t.replace(/(^|[\s(\[—–-])'/g, '$1\u2018').replace(/'/g, '\u2019');
  return t;
}
function runs(t, base = {}) {
  const out = [];
  smart(t).split(/(\*\*[^*]+\*\*|\*[^*]+\*)/).forEach(part => {
    if (!part) return;
    if (/^\*\*[^*]+\*\*$/.test(part)) out.push(new TextRun({ ...base, text: part.slice(2, -2), bold: true }));
    else if (/^\*[^*]+\*$/.test(part)) out.push(new TextRun({ ...base, text: part.slice(1, -1), italics: true }));
    else out.push(new TextRun({ ...base, text: part }));
  });
  return out;
}
function pngSize(file) {
  const b = fs.readFileSync(file);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}
function figure(f) {
  const file = FIG + f.file, { w, h } = pngSize(file);
  let width = TEXT_W_PX, height = Math.round(h * width / w);
  const maxH = 430; if (height > maxH) { height = maxH; width = Math.round(w * height / h); }
  return [
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 240, after: 80 }, keepNext: true,
      children: [new ImageRun({ type: 'png', data: fs.readFileSync(file), transformation: { width, height },
        altText: { title: f.cap, description: f.cap, name: f.file } })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 280 },
      children: [new TextRun({ text: f.cap, font: SANS, size: 16, color: GREY, italics: true })] }),
  ];
}
function partPage(name) {
  return [
    new Paragraph({ pageBreakBefore: true, alignment: AlignmentType.CENTER, spacing: { before: 3600, after: 0 },
      children: [new TextRun({ text: name.split(':')[0].toUpperCase(), font: SANS, size: 20, color: ORANGE, characterSpacing: 60 })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120 },
      children: [new TextRun({ text: name.split(':')[1].trim(), font: SANS, size: 36, bold: true })] }),
  ];
}
function heading(label, name, id) {
  const out = [];
  if (label) out.push(new Paragraph({ pageBreakBefore: true, spacing: { before: 1440, after: 100 }, keepNext: true,
    children: [new TextRun({ text: label.toUpperCase(), font: SANS, size: 18, color: ORANGE, characterSpacing: 50 })] }));
  out.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: !label,
    spacing: label ? { before: 0, after: 480 } : { before: 1440, after: 480 },
    children: [new Bookmark({ id: 'b' + id, children: [new TextRun({ text: name })] })] }));
  return out;
}

// ---------- front matter
const cover = [new Paragraph({ children: [new ImageRun({ type: 'png', data: fs.readFileSync('/home/claude/pdfbuild/cover-c.png'),
  transformation: { width: 576, height: 864 }, altText: { title: 'Cover', description: 'Front cover', name: 'cover' } })] })];

const front = [
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 2400 }, children: [new TextRun({ text: 'Build the Thing That Builds the Things', font: SANS, size: 40, bold: true })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 240 }, children: [new TextRun({ text: 'Go Exponential: From Incremental Progress to Compound Growth', font: SANS, size: 22, color: '444444' })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 960 }, children: [new TextRun({ text: 'ANT SMOOTHEY', font: SANS, size: 20, characterSpacing: 60 })] }),
  new Paragraph({ pageBreakBefore: true, spacing: { before: 6000 }, children: [new TextRun({ text: `Review copy, ${DATE}.`, font: SANS, size: 17, bold: true })] }),
  new Paragraph({ spacing: { before: 120 }, children: [new TextRun({ text: 'This is a work in progress. It holds the chapters agreed so far, before the final polish. Chapters marked \u201Cto come\u201D on the contents page are still being written.', font: SANS, size: 17, color: '444444' })] }),
  new Paragraph({ spacing: { before: 120 }, children: [new TextRun({ text: 'Please don\u2019t share or copy it. Comments and tracked changes are very welcome.', font: SANS, size: 17, color: '444444' })] }),
  new Paragraph({ spacing: { before: 120 }, children: [new TextRun({ text: '\u00A9 Ant Smoothey 2026.', font: SANS, size: 17, color: '444444' })] }),
  // contents
  new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, spacing: { before: 120, after: 240 }, children: [new TextRun('Contents')] }),
];
plan.forEach(group => {
  if (group.part) front.push(new Paragraph({ spacing: { before: 140, after: 40 }, keepNext: true,
    children: [new TextRun({ text: group.part, font: SANS, size: 18, bold: true, color: ORANGE })] }));
  group.items.forEach(([name, id]) => {
    if (id) front.push(new Paragraph({ spacing: { after: 20 }, indent: { left: group.part ? 240 : 0 },
      children: [new InternalHyperlink({ anchor: 'b' + id, children: [new TextRun({ text: smart(name), font: SERIF, size: 20, color: '1a1a1a' })] })] }));
    else front.push(new Paragraph({ spacing: { after: 20 }, indent: { left: group.part ? 240 : 0 },
      children: [new TextRun({ text: smart(name), font: SERIF, size: 20, color: '999999' }), new TextRun({ text: '   to come', font: SANS, size: 15, color: '999999', italics: true })] }));
  });
});

// ---------- body
const body = [];
written.forEach(f => {
  const num = f.slice(0, 2);
  const lines = fs.readFileSync(CH + f, 'utf8').split('\n');
  if (partBefore[num]) body.push(...partPage(partBefore[num]));
  if (num === '13') {
    body.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 600 },
      children: [new TextRun({ text: 'Chapters 9 to 12 are still being written. The story picks up again at chapter 13.', font: SANS, size: 17, color: GREY, italics: true })] }));
  }
  const title = lines[0].replace(/^#\s*/, '').trim();
  let label = '', name = title;
  if (title.includes(':')) { label = title.split(':')[0].trim(); name = title.split(':').slice(1).join(':').trim(); }
  body.push(...heading(label, name, num));
  const figs = figures[num] || [];
  let pIdx = 0, first = true;
  for (let i = 1; i < lines.length; i++) {
    const l = lines[i].trim();
    if (!l) continue;
    if (l.startsWith('<!--')) {
      const m = l.match(/p:\s*\d+-(\d+)/); if (m) pIdx = parseInt(m[1], 10);
      if (/figure fig\S+ goes after this paragraph/.test(l)) figs.filter(x => x.markerAfter).forEach(x => body.push(...figure(x)));
      continue;
    }
    if (l.startsWith('#')) continue;
    body.push(new Paragraph({ style: first ? 'BodyFirst' : 'Body', children: runs(l) }));
    first = false;
    figs.filter(x => (typeof x.after === 'number' && x.after === pIdx) || (typeof x.after === 'function' && x.after(l)))
        .forEach(x => body.push(...figure(x)));
  }
});

// ---------- back matter: glossary and notes
body.push(...heading('', 'Glossary', 'gloss'));
fs.readFileSync(CH + '98-glossary.md', 'utf8').split('\n').map(s => s.trim())
  .filter(s => s.startsWith('**')).forEach(s => body.push(new Paragraph({ style: 'Entry', children: runs(s) })));

body.push(...heading('', 'Notes and further reading', 'notes'));
let inComment = false;
fs.readFileSync(CH + '99-notes.md', 'utf8').split('\n').forEach(raw => {
  const s = raw.trim();
  if (s.startsWith('<!--')) { inComment = !s.includes('-->'); return; }
  if (inComment) { if (s.includes('-->')) inComment = false; return; }
  if (!s || s.startsWith('# ')) return;
  if (s.startsWith('## ')) body.push(new Paragraph({ spacing: { before: 280, after: 100 }, keepNext: true,
    children: [new TextRun({ text: s.slice(3), font: SANS, size: 19, bold: true, color: ORANGE })] }));
  else body.push(new Paragraph({ style: 'Entry', children: runs(s) }));
});
body.push(new Paragraph({ spacing: { before: 480 }, alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: `Review copy, ${DATE}. Not for distribution.`, font: SANS, size: 15, color: GREY })] }));

// ---------- document
const footer = new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
  children: [new TextRun({ children: [PageNumber.CURRENT], font: SANS, size: 16, color: GREY })] })] });
const doc = new Document({
  creator: 'Ant Smoothey', title: 'Build the Thing That Builds the Things (review copy)',
  styles: {
    default: { document: { run: { font: SERIF, size: 22 } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { font: SANS, size: 36, bold: true, color: '141414' },
        paragraph: { spacing: { before: 0, after: 480 }, keepNext: true, outlineLevel: 0 } },
      { id: 'Body', name: 'Body', basedOn: 'Normal', quickFormat: true, run: { font: SERIF, size: 22 },
        paragraph: { spacing: { after: 0, line: 330 }, indent: { firstLine: 360 }, alignment: AlignmentType.JUSTIFIED } },
      { id: 'BodyFirst', name: 'Body First', basedOn: 'Body', quickFormat: true, paragraph: { indent: { firstLine: 0 } } },
      { id: 'Entry', name: 'Entry', basedOn: 'Normal', quickFormat: true, run: { font: SERIF, size: 19 },
        paragraph: { spacing: { after: 140, line: 290 } } },
    ],
  },
  sections: [
    { properties: { page: { size: PAGE, margin: { top: 0, bottom: 0, left: 0, right: 0, header: 0, footer: 0 } } }, children: cover },
    { properties: { type: SectionType.NEXT_PAGE, page: { size: PAGE, margin: MARGIN } }, children: front },
    { properties: { type: SectionType.NEXT_PAGE, page: { size: PAGE, margin: MARGIN, pageNumbers: { start: 1 } } }, footers: { default: footer }, children: body },
  ],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(process.argv[2], b); console.log('written', b.length); });
