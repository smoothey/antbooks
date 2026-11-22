import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
from matplotlib import font_manager as fm
for f in fm.findSystemFonts():
    if 'Inter' in f: fm.fontManager.addfont(f)
plt.rcParams.update({'font.family':'Inter','font.size':12,'svg.fonttype':'none'})
INK,MID,LIGHT,FAINT,ACC='#1E1E1E','#6B6B6B','#BDBDBD','#EFEFEF','#E07A1F'
OUT='/home/claude/antbooks/books/build-the-thing/figures/'
def save(fig,name):
    fig.savefig(OUT+name+'.svg',bbox_inches='tight'); fig.savefig(OUT+name+'.png',dpi=200,bbox_inches='tight',facecolor='white'); plt.close(fig)
def box(ax,x,y,w,h,text,fc='white',ec=INK,lw=1.5,fs=12,bold=False,color=INK):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.08',fc=fc,ec=ec,lw=lw))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs,fontweight='bold' if bold else 'normal',color=color,wrap=True)
def arrow(ax,x1,y1,x2,y2,color=MID):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='-|>',color=color,lw=1.5,mutation_scale=14))

# fig02b how it grew, one problem at a time
steps=[('30 Sep','First\nrepository','a record starts'),('13 Oct',"Charlie's\nsite",'the work'),('16 Oct','Jimmy gets\na name','and a face'),('18 Oct','The\nstore','one place\nfor the truth'),('18 Oct','First\nnight run','22:48 to 23:45'),('19 Oct','Morning\nbrief','and the Hub'),('20 Oct','Share of\na night','our own pace'),('Nov','The\nCockpit','look and talk\nin one place')]
fig,ax=plt.subplots(figsize=(13,3.6)); ax.set_xlim(0,13); ax.set_ylim(-0.1,3.4); ax.axis('off')
ax.plot([0.4,12.6],[1.6,1.6],color=LIGHT,lw=3)
for i,(d,t,s) in enumerate(steps):
    x=0.9+i*1.6
    ax.add_patch(Circle((x,1.6),0.12,color=ACC if t=='The store' else INK))
    ax.text(x,2.05,d,ha='center',fontsize=10,color=MID)
    ax.text(x,1.3,t,ha='center',va='top',fontsize=10.5,fontweight='bold',color=INK)
    ax.text(x,0.62,s,ha='center',va='top',fontsize=9,color=MID)
ax.text(0.4,2.9,'Each piece answered the problem the last one showed up',fontsize=13,color=INK)
save(fig,'fig02b-how-it-grew')

# fig04 one truth, three front doors
fig,ax=plt.subplots(figsize=(9,5)); ax.set_xlim(0,9); ax.set_ylim(0,5); ax.axis('off')
box(ax,3.1,0.5,2.8,1.3,'The store\none place for the truth',fc=FAINT,ec=ACC,lw=2.5,fs=13,bold=True)
doors=[(0.3,'AI chats and night runs\n(through MCP)',''),(3.3,'Scripts and devices\n(through the API)',''),(6.3,'Me\n(through the Hub)','')]
for x,t,s in doors:
    box(ax,x,3.2,2.4,1.1,t,fs=11)
    ax.text(x+1.2,2.75,s,ha='center',fontsize=10,color=MID)
    arrow(ax,x+1.2,3.15,4.5,1.85)
ax.text(4.5,0.15,'Same records, same rules, whichever door you use',ha='center',fontsize=10,color=MID)
save(fig,'fig04-one-truth-three-doors')

# fig08 privacy rings
fig,ax=plt.subplots(figsize=(7,7)); ax.set_xlim(-5,5); ax.set_ylim(-5,5); ax.set_aspect('equal'); ax.axis('off')
rings=[(4.6,'#F4F4F4','Ring 3: the public\npublished pages only, no store access'),(3.5,'#E2E2E2','Ring 2: a project\nits own people'),(2.4,'#C9C9C9','Ring 1: home\nme and Charlie'),(1.3,ACC,'Ring 0\nonly me')]
for r,c,_ in rings: ax.add_patch(Circle((0,0),r,fc=c,ec=INK,lw=1.2))
ax.text(0,0,'Ring 0\nonly me',ha='center',va='center',fontsize=12,fontweight='bold',color='white')
ax.text(0,1.85,'Ring 1\nhome',ha='center',va='center',fontsize=11)
ax.text(0,2.95,'Ring 2: a project',ha='center',va='center',fontsize=11)
ax.text(0,4.05,'Ring 3: the public',ha='center',va='center',fontsize=11)
ax.text(0,-5.3,'Ring 0: only me.  Ring 1: me and Charlie.  Ring 2: a project and its people.\nRing 3: published pages only, no access to the store.\nChecked by the store on every request, not by what an AI is told.',ha='center',va='top',fontsize=10,color=MID)
save(fig,'fig08-privacy-rings')

# fig11 best practice by accident
rows=[('What I did','What it\'s called'),('A stopgap, then pushed for the real fix (the Jade crash)','Problem management'),('An audit tool that listed everything we ran','A configuration database (CMDB)'),('User stories written after the work was done','User stories (usually written first)'),('No releases in the week before a reveal','A change freeze'),('A one-page brief every morning','A daily stand-up'),('Writing down what went wrong and what we changed','A retrospective'),('Recording what we decided and why','Architecture decision records')]
fig,ax=plt.subplots(figsize=(10,5.2)); ax.set_xlim(0,10); ax.set_ylim(0,len(rows)+0.5); ax.axis('off')
for i,(a,b) in enumerate(rows):
    y=len(rows)-i-0.5
    bold=i==0
    if i==0: ax.add_patch(FancyBboxPatch((0,y-0.4),10,0.8,boxstyle='square,pad=0',fc=FAINT,ec='none'))
    ax.text(0.15,y,a,va='center',fontsize=11.5,fontweight='bold' if bold else 'normal',color=INK)
    ax.text(5.9,y,b,va='center',fontsize=11.5,fontweight='bold' if bold else 'normal',color=ACC if not bold else INK)
    if i>0: ax.plot([0,10],[y-0.5,y-0.5],color=LIGHT,lw=0.8)
ax.text(0.15,-0.45,'DRAFT: the list is agreed with Ant when chapter 11 is written',fontsize=9,color=MID)
save(fig,'fig11-best-practice-by-accident')

# fig16 a production line
st=['Research\nthe exam','Plan the\nbook','Write it,\nchapter\nby chapter','Check facts\nand figures','One pull\nrequest to\ngo live','I approve\nwith one tap','Published']
fig,ax=plt.subplots(figsize=(12,2.8)); ax.set_xlim(0,12.2); ax.set_ylim(0,2.8); ax.axis('off')
for i,s in enumerate(st):
    x=0.1+i*1.73
    box(ax,x,0.8,1.45,1.15,s,fc=ACC if i==5 else ('white'),ec=INK,fs=10,color='white' if i==5 else INK,bold=i==5)
    if i<len(st)-1: arrow(ax,x+1.47,1.37,x+1.71,1.37)
ax.text(0.1,2.4,'One repeating piece of work, from idea to published: the machine runs every step but one',fontsize=12)
ax.text(0.1,0.3,'The line keeps changing: each book teaches the next one',fontsize=10,color=MID)
save(fig,'fig16-production-line')

# fig07 needs you mock-up
fig,ax=plt.subplots(figsize=(7,6.4)); ax.set_xlim(0,7); ax.set_ylim(0,6.4); ax.axis('off')
ax.add_patch(FancyBboxPatch((0.1,0.1),6.8,6.2,boxstyle='round,pad=0,rounding_size=0.15',fc='white',ec=INK,lw=1.5))
ax.add_patch(FancyBboxPatch((0.1,5.6),6.8,0.7,boxstyle='square,pad=0',fc=FAINT,ec='none'))
ax.text(0.4,5.95,'Needs you',fontsize=15,fontweight='bold'); ax.text(6.6,5.95,'4',fontsize=13,ha='right',color=ACC,fontweight='bold')
items=[('Merge','Photo organiser: three fixes on one pull request','2 min'),('Agree','Charlie\'s site: give the second shift 10 changes a night','1 min'),('Try','Camera app: test the new lens warning on your phone','5 min'),('Discuss','Book: which night should chapter 6 follow?','talk')]
for i,(k,t,m) in enumerate(items):
    y=4.75-i*1.2
    ax.add_patch(FancyBboxPatch((0.4,y-0.38),1.1,0.5,boxstyle='round,pad=0,rounding_size=0.1',fc=ACC if k=='Merge' else 'white',ec=INK,lw=1))
    ax.text(0.95,y-0.13,k,ha='center',va='center',fontsize=10.5,color='white' if k=='Merge' else INK,fontweight='bold')
    ax.text(1.75,y,t,fontsize=10.5,va='center',wrap=True)
    ax.text(6.6,y-0.35,m,fontsize=9.5,ha='right',color=MID)
    ax.plot([0.4,6.6],[y-0.62,y-0.62],color=LIGHT,lw=0.8)
ax.text(0.4,0.3,'Illustration: items are examples in the style of the real list',fontsize=8.5,color=MID)
save(fig,'fig07-needs-you')
print('ok')
