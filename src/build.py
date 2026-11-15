from cases import CASES, case_html, SLUG
BAR='''<header class="bar static"><span class="who"><a class="me" href="#home">David Shih</a><span class="tag">Purveyor of fine memes since the early aughts.</span></span><nav aria-label="Primary"><a href="#work">Work</a><a href="#about">About</a><a href="#resume">Resume</a></nav></header>'''
import os, shutil
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.dirname(HERE)            # repo root, which GitHub Pages serves
W=os.path.join(HERE,'work','')       # home tile images and portraits
os.makedirs(os.path.join(OUT,'img','home'),exist_ok=True)
def b(n,mime=None):
    # copy the image into the site and return its path (images used to be embedded in the HTML)
    shutil.copyfile(W+n,os.path.join(OUT,'img','home',n)); return 'img/home/'+n
img={k:b(k+'.webp','image/webp') for k in ['statefarm','jeep','camelot','tepper','filtereasy']}
img.update({k:b(k+'.jpg') for k in ['crackerbarrel','samsung','sony','adlandgigs','jimbeam','tusk','pocket']})
head=b('profile_edge.webp','image/webp')
S='https://www.davidvshih.com/'
# key, theta deg (0 = toward viewer, 90 = screen right, 180 = behind him), radius, y offset, base width, name, href, shape
cards=[
 ('samsung',17,400,232,168,'Samsung',S+'samsung-times-square/',''),
 ('jeep',36,460,-219,158,'Jeep',S+'jeep/',''),
 ('camelot',60,465,-60,166,'Second Nature',S+'second-nature/',''),
 ('adlandgigs',84,462,103,120,'AdLand Gigs',S+'adlandgigs/','sq'),
 ('statefarm',68,412,228,160,'State Farm',S+'state-farm/',''),
 ('pocket',96,544,-334,118,'Pocket Agency','https://www.thepocketagency.com/','sq'),
 ('tepper',118,235,-160,150,'Carnegie Mellon: Tepper School',S+'tepper-school-of-business/',''),
 ('filtereasy',210,480,-330,150,'Filter Easy',S+'filter-easy/',''),
 ('crackerbarrel',140,480,-40,150,'Cracker Barrel',S+'cracker-barrel/',''),
 ('tusk',150,470,175,150,'Tusk Wine',S+'tusk-wine/',''),
 ('sony',210,480,-330,150,'Sony Alpha',S+'sony-alpha-camera/',''),
 ('jimbeam',218,520,280,100,'Jim Beam Honey',S+'jim-beam/','tall'),
]
hover={'samsung':('The Galaxy S III launch that took over Times Square.','Campaign · Brand launch'),
 'jeep':('Mars Rover. Film for BBDO Detroit.','Film · Broadcast'),
 'camelot':('Camelot. A brand film from the in-house studio.','Film · In-house'),
 'statefarm':('NFL sponsorship work for DDB.','Campaign · Sponsorship'),
 'adlandgigs':('A daily job digest for ad people, built with AI.','Product · AI build'),
 'pocket':('An AI marketing service for small businesses.','Product · AI build'),
 'tepper':('A brand vision for the business school.','Brand · Anthem film'),
 'filtereasy':('A full brand refresh for a filter company.','Brand · Identity'),
 'crackerbarrel':('Campfire Meals relaunch. The Worst Camper in the World.','Campaign · Relaunch'),
 'tusk':('Packaging for a boxed set.','Design · Packaging'),
 'sony':('Launch of Sony\'s first digital SLR.','Campaign · Print'),
 'jimbeam':('Sweet. With an uppercut.','Campaign · Print')}
def card(c,i):
    k,th,R,y,w,name,href,shape=c
    media = f'<img src="{img[k]}" alt="">' if k in img else '<span class="mono" aria-hidden="true">PA</span>'
    href='#'+SLUG[k]
    tag,attr=('a',f' href="{href}"')
    fix=' data-fx="104" data-fy="124"' if k=='filtereasy' else (' data-fx="305" data-fy="146" data-pin="mid"' if k=='sony' else '')
    return f'<li class="orb {shape}" data-th="{th}" data-r="{R}" data-y="{y}" data-w="{w}"{fix}><{tag} class="tile"{attr} aria-label="{name}"><span class="media">{media}</span><span class="info"><span class="nm">{name}</span><span class="ln">{hover[k][0]}</span><span class="tg">{hover[k][1]}</span></span></{tag}></li>'
orbs='\n'.join(card(c,i) for i,c in enumerate(cards))
desc={'samsung':'Galaxy S III launch in Times Square','jeep':'Film, BBDO Detroit','camelot':'In-house agency and production studio','statefarm':'NFL sponsorship, DDB',
 'adlandgigs':'AI-assisted job digest for ad people','pocket':'AI marketing service for small businesses','tepper':'Brand vision for Carnegie Mellon\'s business school',
 'crackerbarrel':'Campfire Meals relaunch','tusk':'','sony':'Launch of Sony\'s first digital SLR, Bagby','filtereasy':'Brand refresh, WMH','jimbeam':'Bourbon with honey campaign, Proof'}
extra=[('DePaul University','Branding campaign','#depaul'),
 ('Princeton University','Branding and annual giving campaign, Digital Pulp','#princeton'),
 ('TransUnion','Rebrand and website overhaul, Avenue','#transunion'),
 ('Equal','Rebrand for the 80-year-old sweetener','#equal'),
 ('Samsung Facebook','Interactive Galaxy phone guide inside Facebook','#samsung-facebook'),
 ('City of Chicago Tech Plan','Print and web, Digitas','#chicago-tech-plan'),
 ('Farm to Fork','Launch of Mizkan\'s premium pasta sauce','#farm-to-fork'),
 ('Coleman','Kelly Award finalist, BBDO','#coleman'),
 ('The reel','Selected commercials','#reel')]
allrows=[(c[5],desc.get(c[0],''),'#'+SLUG[c[0]]) for c in cards]+extra
rows='\n'.join(f'<li><span class="n">{i+1:02d}</span><span class="t">'+(f'<a href="{h}">{n}</a>' if h else n)+f'</span><span class="d">{d}</span>'+(f'<a href="{h}">Open</a>' if h else '<span class="soon">Page to come</span>')+'</li>' for i,(n,d,h) in enumerate(allrows))
import sys, re
theme=sys.argv[1] if len(sys.argv)>1 else 'gold'
tpl=open(os.path.join(HERE,'template.html')).read()
if theme in ('orange','mandarin','gold','brown'):
    for a,c in [("--pop:#1c2bc9;","--pop:#ffffff;"),
                ("--bg:#ffffff; --ink:#0b0b0d; --soft:#6b6f80; --rule:#e3e4ea; --accent:#1c2bc9; --navy:#14254f; --signal:#ffd23f;","--bg:#f15a0a; --ink:#0b0b0d; --soft:#3d1803; --rule:rgba(11,11,13,.28); --accent:#0b0b0d; --navy:#ffffff; --signal:#f15a0a;"),
                ("box-shadow:5px 12px 18px rgba(11,11,13,.34),1px 2px 4px rgba(11,11,13,.22);","box-shadow:0 0 0 1.5px rgba(255,255,255,.92),6px 14px 20px rgba(60,18,0,.5),1px 2px 4px rgba(60,18,0,.35);"),
                ("box-shadow:8px 18px 28px rgba(11,11,13,.4),1px 2px 4px rgba(11,11,13,.2)}","box-shadow:0 0 0 1.5px #fff,10px 20px 30px rgba(60,18,0,.55),1px 2px 4px rgba(60,18,0,.3)}"),
                (".mono{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:var(--signal);color:var(--ink);",".mono{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:var(--ink);color:#fff;"),
                ("<title>David Shih portfolio prototype</title>","<title>David Shih portfolio prototype, orange</title>")]:
        assert a in tpl, a[:40]; tpl=tpl.replace(a,c)
if theme=='mandarin':
    over="""
/* palette: Mandarin Orange #FD550A, Forest Green #005C47, Crest Yellow #E0F354 */
:root{--bg:#FD550A;--soft:#3a1602;--navy:#E0F354;--signal:#E0F354;--pop:#E0F354;--forest:#005C47}
.band{background:var(--forest)}
.clients li{color:#fff}
.clients li:nth-child(even){color:#E0F354}
.tile{background:var(--forest)}
.info .tg{color:#E0F354}
.cbtn{border-color:var(--forest)}
.cbtn.mail{background:#E0F354;color:var(--forest);box-shadow:5px 5px 0 var(--forest)}
.cbtn.mail:hover,.cbtn.mail:focus-visible{box-shadow:2px 2px 0 var(--forest)}
.cbtn.li{background:var(--forest);color:#E0F354;box-shadow:5px 5px 0 #E0F354}
.cbtn.li:hover,.cbtn.li:focus-visible{box-shadow:2px 2px 0 #E0F354}
.cbtn .in{background:#E0F354;color:var(--forest)}
.btn{background:var(--forest);border-color:var(--forest)}
.btn.ghost{color:var(--forest)}
.resume h2{border-bottom-color:var(--forest);color:var(--forest)}
.index{border-top-color:var(--forest)}
.about .aside{border-left-color:var(--forest)}
:root{--frame:var(--forest);--frameshadow:#E0F354}
:focus-visible{outline-color:var(--forest)}
"""
    assert tpl.count('</style>')==1
    tpl=tpl.replace('</style>',over+'</style>').replace('portfolio prototype, orange</title>','portfolio prototype, mandarin</title>')
if theme=='gold':
    over="""
/* palette: Brown #603E1E, Pale Gold #F1D9A8, Glowing Gold #FFC34D */
:root{--bg:#FFC34D;--soft:#603E1E;--rule:rgba(96,62,30,.32);--navy:#603E1E;--signal:#FFC34D;--pop:#0b0b0d;--brown:#603E1E;--pale:#F1D9A8}
.band{background:var(--brown)}
.clients li{color:var(--pale)}
.clients li:nth-child(even){color:#FFC34D}
.tile{background:var(--brown);color:var(--pale)}
.info .ln{color:rgba(241,217,168,.9)}
.info .tg{color:#FFC34D;border-top-color:rgba(241,217,168,.3)}
.cbtn{border-color:var(--brown)}
.cbtn.mail{background:var(--pale);color:var(--brown);box-shadow:5px 5px 0 var(--brown)}
.cbtn.mail:hover,.cbtn.mail:focus-visible{box-shadow:2px 2px 0 var(--brown)}
.cbtn.li{background:var(--brown);color:var(--pale);box-shadow:5px 5px 0 #0b0b0d}
.cbtn.li:hover,.cbtn.li:focus-visible{box-shadow:2px 2px 0 #0b0b0d}
.cbtn .in{background:var(--pale);color:var(--brown)}
.btn{background:var(--brown);border-color:var(--brown);color:var(--pale)}
.btn.ghost{color:var(--brown);background:transparent}
.btn:hover{background:var(--pale);color:var(--brown);border-color:var(--pale)}
.resume h2{border-bottom-color:var(--brown);color:var(--brown)}
.index{border-top-color:var(--brown)}
.about .aside{border-left-color:var(--brown)}
:root{--frame:var(--brown);--frameshadow:var(--brown)}
.me,.bar nav a{color:var(--brown)}
:focus-visible{outline-color:var(--brown)}
"""
    assert tpl.count('</style>')==1
    tpl=tpl.replace('</style>',over+'</style>').replace('portfolio prototype, orange</title>','portfolio prototype, gold</title>')
if theme=='brown':
    over="""
/* palette, brown-led: Brown #603E1E background, Pale Gold #F1D9A8 text, Glowing Gold #FFC34D accent */
:root{--bg:#603E1E;--soft:#d6bb88;--rule:rgba(241,217,168,.24);--navy:#FFC34D;--signal:#FFC34D;--pop:#F1D9A8;--brown:#603E1E;--pale:#F1D9A8;--gold:#FFC34D;color-scheme:dark}
body{color:var(--pale)}
.stage{background:radial-gradient(85% 95% at 16% 64%,#86592f 0%,#6c4622 38%,#603E1E 66%)}
.me,.bar a.me,.bar nav a{color:var(--pale)}
.bar a:hover{color:var(--gold)}
.headline,.proof{color:var(--pale)}
.band{background:var(--gold)}
.clients li{color:var(--brown)}
.clients li:nth-child(even){color:#0b0b0d}
.tile{background:var(--pale);color:var(--brown);box-shadow:0 0 0 1.5px rgba(241,217,168,.92),6px 14px 22px rgba(0,0,0,.5),1px 2px 4px rgba(0,0,0,.4)}
.orb:hover .tile,.orb:focus-within .tile{box-shadow:0 0 0 1.5px var(--pale),10px 20px 32px rgba(0,0,0,.6),1px 2px 4px rgba(0,0,0,.4)}
.info .ln{color:rgba(96,62,30,.92)}
.info .tg{color:var(--brown);border-top-color:rgba(96,62,30,.3)}
.cbtn{border-color:var(--pale)}
.cbtn.mail{background:var(--gold);color:var(--brown);box-shadow:5px 5px 0 var(--pale)}
.cbtn.mail:hover,.cbtn.mail:focus-visible{box-shadow:2px 2px 0 var(--pale)}
.cbtn.li{background:var(--pale);color:var(--brown);box-shadow:5px 5px 0 var(--gold)}
.cbtn.li:hover,.cbtn.li:focus-visible{box-shadow:2px 2px 0 var(--gold)}
.cbtn .in{background:var(--brown);color:var(--pale)}
.btn{background:var(--pale);border-color:var(--pale);color:var(--brown)}
.btn.ghost{color:var(--pale);background:transparent}
.btn:hover{background:var(--gold);color:var(--brown);border-color:var(--gold)}
.resume h2{border-bottom-color:var(--pale);color:var(--gold)}
.index{border-top-color:var(--pale)}
.about .aside{border-left-color:var(--gold)}
:root{--frame:var(--pale);--frameshadow:var(--gold)}
:focus-visible{outline-color:var(--gold)}
"""
    assert tpl.count('</style>')==1
    tpl=tpl.replace('</style>',over+'</style>').replace('portfolio prototype, orange</title>','portfolio prototype, brown</title>')
html=tpl.replace('{{ORBS}}',orbs).replace('{{HEAD}}',head).replace('{{HEAD2}}',b('about.jpg')).replace('{{CASES}}','\n'.join(case_html(c,i,BAR) for i,c in enumerate(CASES))).replace('{{ROWS}}',rows)
html=re.sub(r'<title>.*?</title>','<title>David Shih, creative leader and author</title>',html,count=1)
open(os.path.join(OUT,'index.html'),'w').write(html); print('index.html',len(html)//1024,'KB, theme',theme)

# Old Squarespace addresses and plain /slug/ addresses forward to the hash routes
OLD={'about-1':'about','about':'about','brands-1':'work','resume':'resume','work':'work',
 'adlandgigs':'adland-gigs','depaul-university':'depaul','sony-alpha-camera':'sony','samsung-times-square':'samsung',
 'equal-rebrand':'equal','my-reel':'reel','coleman-kelly-finalist':'coleman','city-of-chicago-tech-plan':'chicago-tech-plan',
 'samsung-galaxy-facebook':'samsung-facebook','tepper-school-of-business':'tepper'}
for c in CASES: OLD.setdefault(c['slug'],c['slug'])
STUB='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>David Shih</title><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=/#{h}"><script>location.replace("/#{h}")</script></head><body><a href="/#{h}">Continue to the page</a></body></html>'
for path,h in OLD.items():
    os.makedirs(os.path.join(OUT,path),exist_ok=True)
    open(os.path.join(OUT,path,'index.html'),'w').write(STUB.replace('{h}',h))
open(os.path.join(OUT,'404.html'),'w').write(STUB.replace('{h}','home'))
open(os.path.join(OUT,'.nojekyll'),'w').write('')
print(len(OLD),'redirects')
