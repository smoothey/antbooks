import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
for f in fm.findSystemFonts():
    if 'Inter' in f: fm.fontManager.addfont(f)
plt.rcParams.update({'font.family':'Inter','font.size':13,'axes.edgecolor':'#6B6B6B','axes.labelcolor':'#1E1E1E','xtick.color':'#1E1E1E','ytick.color':'#1E1E1E','axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none'})
INK,MID,LIGHT,FAINT,ACC='#1E1E1E','#6B6B6B','#BDBDBD','#E6E6E6','#E07A1F'
OUT='/home/claude/antbooks/books/build-the-thing/figures/'
def save(fig,name):
    fig.savefig(OUT+name+'.svg',bbox_inches='tight'); fig.savefig(OUT+name+'.png',dpi=200,bbox_inches='tight',facecolor='white'); plt.close(fig)

# fig03b changes per week
wk=['28 Sep','5 Oct','12 Oct','19 Oct','26 Oct','2 Nov','9 Nov','16 Nov']; v=[140,107,397,476,688,744,573,929]
fig,ax=plt.subplots(figsize=(8,4.2))
cols=[LIGHT]*2+[MID]*5+[ACC]
ax.bar(wk,v,color=cols,width=0.65)
for i,x in enumerate(v): ax.text(i,x+15,str(x),ha='center',fontsize=11,color=INK)
ax.set_ylabel('Changes saved'); ax.set_xlabel('Week starting (2026)')
ax.annotate("Charlie's site and\nthe store begin",xy=(1.8,300),xytext=(-0.3,700),fontsize=11,color=MID,arrowprops=dict(arrowstyle='-',color=MID))
ax.set_ylim(0,1020); ax.tick_params(length=0)
save(fig,'fig03b-changes-per-week')

# fig03a incremental vs compound
import numpy as np
x=np.linspace(0,10,200)
fig,ax=plt.subplots(figsize=(8,4.6))
inc=np.minimum(x*0.9,5.0)
comp=0.35*(np.exp(0.33*x)-1)
ax.plot(x,inc,color=MID,lw=3)
ax.plot(x,comp,color=ACC,lw=3.5)
ax.axhline(5.0,color=LIGHT,ls='--',lw=1.5)
ax.text(0.2,5.25,'The ceiling: the hours you have',color=MID,fontsize=11)
ax.text(6.4,2.5,'Incremental:\nadding hours',color=MID,fontsize=12)
ax.text(7.0,8.2,'Compound:\nadding things\nthat add',color=ACC,fontsize=12,fontweight='bold')
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('Time'); ax.set_ylabel('What gets done')
ax.set_ylim(0,9.6); ax.set_xlim(0,10)
save(fig,'fig03a-incremental-vs-compound')

# fig05a minutes used per night
import datetime as dt
nights=[('2026-10-20',274),('2026-10-21',255),('2026-10-22',357),('2026-10-23',373),('2026-10-24',301),('2026-10-25',286),('2026-10-26',317),('2026-10-27',230),('2026-10-28',324),('2026-10-29',282),('2026-10-30',277),('2026-10-31',179),('2026-11-01',262),('2026-11-02',177),('2026-11-03',321),('2026-11-04',517),('2026-11-05',443),('2026-11-06',210),('2026-11-07',227),('2026-11-08',278),('2026-11-09',258),('2026-11-10',268),('2026-11-11',255),('2026-11-12',216),('2026-11-13',253),('2026-11-14',219),('2026-11-15',252),('2026-11-16',257),('2026-11-17',246),('2026-11-18',372),('2026-11-19',311),('2026-11-20',282),('2026-11-21',294)]
d=[dt.date.fromisoformat(a) for a,_ in nights]; m=[b for _,b in nights]
fig,ax=plt.subplots(figsize=(9,4.4))
ax.axhspan(0,480,color=FAINT,zorder=0)
ax.axhline(480,color=MID,lw=1.2); ax.axhline(360,color=MID,ls='--',lw=1.2)
ax.plot(d,m,color=INK,lw=2,marker='o',ms=4)
ax.plot([d[15]],[m[15]],marker='o',ms=8,color=ACC)
ax.text(d[0],492,'480 minutes: a whole night',fontsize=10,color=MID)
ax.text(d[0],378,'75%: the brief warns below this',fontsize=10,color=MID)
ax.annotate('4 Nov: borrowed time,\n517 minutes',xy=(d[15],517),xytext=(d[17],530),fontsize=10,color=ACC,arrowprops=dict(arrowstyle='-',color=ACC))
ax.annotate('Away mode:\nwork waits on my merges',xy=(d[22],216),xytext=(d[19],80),fontsize=10,color=MID,arrowprops=dict(arrowstyle='-',color=MID))
ax.set_ylim(0,600); ax.set_ylabel('Minutes used')
import matplotlib.dates as mdates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%-d %b')); ax.tick_params(length=0)
save(fig,'fig05a-minutes-per-night')

# fig05b share of a night
fig,ax=plt.subplots(figsize=(8,2.6))
shares=[('1/16',1/16),('1/8',1/8),('1/4',1/4),('1/2',1/2),('1 night',1)]
y=0
for i,(lab,s) in enumerate(shares):
    ax.barh(4-i,s,color=ACC if lab=='1 night' else MID,height=0.6)
    ax.text(s+0.015,4-i,lab,va='center',fontsize=12)
ax.set_xlim(0,1.15); ax.axis('off')
ax.text(0,5.0,'How big is a piece of work? A share of one night of building.',fontsize=12,color=INK)
save(fig,'fig03c-share-of-a-night')

# fig06 a night hour by hour (18 Nov 2026)
runs=[("Charlie's site",'22:47',49),("Roblox game",'23:51',10),("Camera app",'00:07',46),("Study guides",'00:23',10),("Photo organiser",'00:53',35),("Charlie's site (2)",'01:37',112),("Photo organiser (2)",'02:13',27),("Camera app (2)",'02:37',25),("Jimmy",'02:53',19),("Jimmy (2)",'03:22',27),("Roblox game (2)",'03:47',3),("Study guides (late)",'04:47',9)]
def mins(t):
    h,mm=map(int,t.split(':')); v=h*60+mm
    return v-22*60 if h>=12 else v+120
fig,ax=plt.subplots(figsize=(9,5.2))
for i,(lab,t,dur) in enumerate(runs):
    s=mins(t); ax.barh(len(runs)-1-i,dur,left=s,color=ACC if 'Charlie' in lab else MID,height=0.6)
    ax.text(s-4,len(runs)-1-i,lab,ha='right',va='center',fontsize=10)
for t,lab in [('23:15','I merge'),('23:53','I merge')]:
    ax.axvline(mins(t),color=LIGHT,ls=':',lw=1.2)
ax.text(mins('23:53')+4,len(runs)-1.6,'my two merges\nbefore bed',fontsize=9,color=MID)
ax.axvline(mins('06:13'),color=INK,lw=1.2); ax.text(mins('06:13')-3,len(runs)-0.4,'06:13 morning brief',ha='right',fontsize=10)
ticks=['22:00','23:00','00:00','01:00','02:00','03:00','04:00','05:00','06:00']
ax.set_xticks([mins(t) for t in ticks]); ax.set_xticklabels(ticks); ax.set_yticks([])
ax.set_xlim(-130,mins('06:40')); ax.spines['left'].set_visible(False); ax.tick_params(length=0)
ax.set_title('One night, 18 November 2026: 372 of 480 minutes used',loc='left',fontsize=13,pad=18)
save(fig,'fig06-a-night-hour-by-hour')

# fig10 the lesson logged seven times
ds=['2026-10-19','2026-10-23','2026-10-27','2026-10-31','2026-11-12','2026-11-19','2026-11-21']
dd=[dt.date.fromisoformat(x) for x in ds]
fig,ax=plt.subplots(figsize=(9,2.8))
ax.axhline(0,color=LIGHT,lw=2)
for i,x in enumerate(dd):
    ax.plot([x],[0],marker='o',ms=12,color=ACC if i==6 else INK)
    ax.text(x,0.35 if i%2==0 else -0.55,x.strftime('%-d %b'),ha='center',fontsize=10)
ax.text(dd[0],1.0,'"One-off reminders made in a chat skip the Hub register"',fontsize=12,color=INK)
ax.text(dd[0],0.7,'The same lesson, written down seven times in five weeks',fontsize=10,color=MID)
ax.set_ylim(-1,1.3); ax.axis('off')
save(fig,'fig10-lesson-seven-times')
print('ok')

# figclose lines to date (closing chapter), stacked by project (like the Hub's Wall)
import json, datetime as dt, matplotlib.dates as mdates
L=json.load(open(OUT+'figclose-lines-to-date.json'))
dd=[dt.date.fromisoformat(x) for x in L['days']]
order=["Charlie's site",'Jimmy','Photo organiser','Roblox game','Study guides']
cols={"Charlie's site":MID,'Jimmy':ACC,'Photo organiser':LIGHT,'Roblox game':FAINT,'Study guides':INK}
fig,ax=plt.subplots(figsize=(9,4.8))
ys=[L['series'][k] for k in order]
ax.stackplot(dd,ys,colors=[cols[k] for k in order],edgecolor='white',linewidth=0.6)
tot=[sum(v) for v in zip(*ys)]
base=0
for k,y in zip(order,ys):
    top=base+y[-1]; mid=(base+top)/2
    ax.text(dd[-1]+dt.timedelta(days=1),mid if y[-1]>20000 else top+4000,f"{k}  {y[-1]:,}",va='center',fontsize=10.5,color=ACC if k=='Jimmy' else INK,fontweight='bold' if k=='Jimmy' else 'normal')
    base=top
ax.text(dd[0],tot[-1]*0.93,f"{tot[-1]:,} lines",fontsize=20,fontweight='bold',color=INK)
ax.text(dd[0],tot[-1]*0.84,'1 Oct to 22 Nov 2026, five projects',fontsize=10.5,color=MID)
ax.annotate('18 Oct: the first night',xy=(dt.date(2026,10,18),tot[17]),xytext=(dt.date(2026,10,9),tot[-1]*0.45),fontsize=10,color=MID,arrowprops=dict(arrowstyle='-',color=MID))
ax.set_xlim(dd[0],dd[-1]); ax.set_ylim(0,tot[-1]*1.02)
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v,p:"0" if v==0 else f"{int(v/1000)}k"))
ax.set_ylabel('Lines written, to date')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%-d %b')); ax.tick_params(length=0)
save(fig,'figclose-lines-to-date')
