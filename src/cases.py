# Case study pages: slug, tile key, name, headline second line, kicker, hero, body paragraphs, meta rows, films, gallery, external link
V='https://vimeo.com/'
CASES=[
 dict(slug='samsung',key='samsung',name='Samsung',line='The Galaxy S III launch that took over Times Square.',tag='Campaign · Brand launch',hero='samsung-1.jpg',
  body=['When Samsung launched their flagship phone, the Galaxy S III, they asked us to create a Times Square event that had never been done before—based on the sharing capabilities of the phone. So we asked ourselves, what do people always do in Times Square? They take pictures.',
        'And then, we took it to extremes.',
        'Four days in Times Square later and with over 1,200 folks sharing their best moves to the giant Samsung screen—it was part of Samsung’s biggest mobile phone launch ever.'],
  meta=[('Role','Creative Director'),('Agency','Razorfish')],films=[('Watch the film',V+'47114738')],gallery=['samsung-2.jpg','samsung-3.jpg'],gclass=''),
 dict(slug='jeep',key='jeep',name='Jeep',line='Mars Rover, and a few years of very good cars.',tag='Film · Print',hero='jeep-1.jpg',film=('318806313',540,360,'Mars Rover, the Jeep commercial'),
  body=['I’m a car buff. I was lucky enough to work on Jeep for a few years at BBDO Detroit. Jeep was and still is one of the best car brands ever. We had the pleasure of shooting a few spots with Michael Bay. He gave us some of the footage from Armageddon and even flipped an 18-wheeler for us. Good times.'],
  meta=[('Role','Associate Creative Director'),('Agency','BBDO Detroit')],films=[('Watch Mars Rover with sound',V+'318806313'),('Watch Murphy’s Law',V+'319094465')],gallery=['jeep-1.jpg','jeep-2.jpg','jeep-3.jpg','jeep-4.jpg','jeep-5.jpg'],gclass=''),
 dict(slug='second-nature',key='camelot',name='Second Nature',line='Leading brand and creative at a PE-backed company.',tag='Executive leadership · In-house',hero='sn-4.jpg',
  body=['Second Nature is a private-equity-backed property technology company serving property managers across the country.',
        'As Executive Creative Director, I owned the brand and everything the company said in public, through a period when it grew from a set of products into a platform.',
        '## Repositioning the company',
        'I worked with the founder and the C-suite to reposition Second Nature from a product suite to a single platform. That meant one brand narrative and one visual system, built so every team could use them without rewriting them.',
        'It also meant changing how the company sold. We moved from sales-led messaging to messaging built on the product and its value to property managers and owners.',
        '## Building the studio',
        'I built and led the in-house agency and production studio: designers, writers, illustrators, videographers, motion artists, and photographers. It carried the company’s campaigns from concept through production, and managed outside agencies where they were the better choice.',
        'I put in the intake and prioritization systems that let a small team handle a high volume of work without losing speed or accountability.',
        '## Working with leadership',
        'I was a senior communications partner to the VP and C-suite team. That covered corporate messaging and executive presentations, plus the sales materials that turned strategy into something a customer would believe.',
        'As the organization changed and products were added, my job was to keep the brand consistent while the company moved around it.',
        '## Staying close to the work',
        'I stayed hands-on in concepting and art direction throughout. Camelot, the film on this page, came out of that studio.',
        'The company’s promise is a triple win for residents, property managers, and owners. The brand had to make that promise clear to all three.'],
  meta=[('Role','Executive Creative Director'),('Tenure','March 2020 to January 2026'),('Company','PE-backed property technology, Raleigh'),('Worked with','Founder and C-suite'),('Led','In-house agency and production studio')],films=[('Watch Camelot',V+'693107508')],gallery=['sn-loop.webp','sn-1.jpg','sn-2.jpg','sn-3.jpg'],gclass=''),
 dict(slug='state-farm',key='statefarm',name='State Farm',line='NFL sponsorship work for DDB.',tag='Campaign · Sponsorship',hero='sf-1.jpg',
  body=['State Farm is a major sponsor of the NFL. Why? Because football is awesome.'],
  meta=[('Role','Creative Director'),('Agency','DDB'),('Credits','Alex Zamiar, Art Director. Jonathan Richman, Copywriter. John Siebert, GCD. Liat Ebersohl, Producer.')],films=[('Watch film one',V+'85062379'),('Watch film two',V+'85062233')],gallery=['sf-loop.webp'],gclass='one'),
 dict(slug='adland-gigs',key='adlandgigs',name='AdLand Gigs',line='A job search secret weapon for creative and marketing people.',tag='Product · AI build',hero=None,
  body=['It’s brutally hard to find a good marketing job right now. So I built myself a secret weapon.',
        'AdLand Gigs is an AI-assisted job discovery platform for creative, brand, marketing, strategy, content, design, and growth roles. It scans public job sources, filters for roles that are actually relevant to marketing people, and packages them into a simple daily digest.',
        'I haven’t coded a day in my life, unless you count writing BASIC in middle school a long time ago. But I’m an experienced creative leader who knows how to define a problem, shape a product, write with precision, test an idea, and use AI as a working partner.',
        'I built AdLand Gigs using a lean modern stack: Python, GitHub, Railway, automated scrapers, job feed parsing, AI-assisted filtering, email delivery, and a Squarespace/Wix-style front-end workflow. With AI’s help, I was able to architect the system, troubleshoot the code, refine the logic, and keep improving the product without pretending to be a software engineer.',
        'For me, AdLand Gigs is more than a side project. It’s a working example of how I think modern creative leadership is changing.',
        'Today’s creative leaders need taste, strategy, storytelling, and craft. But they also need enough technical fluency to build momentum. They need to know how to spot a problem, use AI intelligently, prototype a system, and turn an idea into something real without waiting for a perfect brief, a massive team, or a six-month roadmap.',
        'AdLand Gigs started as a personal pain point. It became a product. And it is still evolving.'],
  meta=[('Role','Founder, builder'),('Stack','Python, GitHub, Railway')],films=[],gallery=[],gclass='',side='adland-1.jpg'),
 dict(slug='pocket-agency',key='pocket',name='Pocket Agency',line='The marketing department for small businesses.',tag='Product · AI build',hero='pocket-2.jpg',
  body=['Most small businesses can’t afford an agency and don’t have time to be one. So I built them one.',
        'Pocket Agency is an AI marketing service for small businesses. It studies a business and its competitors, picks the one marketing move worth making that week, and makes the finished ad. The owner approves it and posts it. Nothing goes out until they say so.',
        'I still haven’t coded a day in my life. What I have is a career spent learning what a good ad is and what a bad one costs.',
        'I built Pocket Agency with Claude and ChatGPT as working partners, on GitHub and Railway, with a PostgreSQL database behind it. Claude writes and ships the code. ChatGPT drafts the industry briefs. I write the tickets, set the standards, and decide what is good enough to send. There are a few hundred tickets so far.',
        'Most of my work is teaching it taste. It works from twelve advertising principles I pulled from people like Ogilvy and Bernbach. It takes its art direction from the business’s own website, so a taco shop doesn’t come out looking like a yoga studio. It has hard rules. Never invent a product or a picture of the owner. Never show a room that doesn’t exist. Food has to look like something you want to eat. If an ad fails a truth check, it doesn’t ship.',
        'For me, Pocket Agency is the agency model rebuilt for a business with no marketing budget. It is also the clearest example I have of what a creative director does when the team is software.',
        'The job turns out to be the same one. Set the bar, and say no to the work that isn’t there yet.',
        'Pocket Agency started as a question about who gets good advertising. It became a product. It is live and still getting better.'],
  meta=[('Role','Founder'),('Company','Paladin House'),('Built with','Claude, ChatGPT'),('Stack','GitHub, Railway, PostgreSQL')],films=[],gallery=[],gclass='',side='pocket-1.jpg',link=('Visit thepocketagency.com','https://www.thepocketagency.com/')),
 dict(slug='tepper',key='tepper',name='Carnegie Mellon: Tepper School',line='A brand vision for the business school.',tag='Brand · Anthem film',hero='tepper-loop.webp',
  body=['The Tepper School of Business at Carnegie Mellon wanted to update their image.','They asked us to create a modern, exciting vision of what their brand could mean for a next generation of leaders. This is what we delivered.'],
  meta=[('Client','Tepper School of Business, Carnegie Mellon University')],films=[('Watch the film',V+'601354341')],gallery=[],gclass=''),
 dict(slug='filter-easy',key='filtereasy',name='Filter Easy',line='Can air and fridge filters be sexy? We asked, why not?',tag='Brand · Identity',hero='fe-loop.mp4',
  body=['After 8 years in the DTC market, it was time for a re-brand. I worked with our agency, WMH in Raleigh, to come up with a new logo and fun branding elements. From there, we designed all new packaging and shot custom photography. Then we built a fun website to better capture our youthful brand. After all, if you can’t have fun with air and fridge filters, you’re just doing it wrong.'],
  meta=[('Role','Executive Creative Director'),('Agency','WMH, Raleigh'),('Credits','Chloe Holzapfel, Filter Easy Design Director.')],films=[],gallery=['fe-magic.webp','fe-5.jpg','fe-1.jpg','fe-2.jpg','fe-3.jpg','fe-4.jpg'],gclass=''),
 dict(slug='cracker-barrel',key='crackerbarrel',name='Cracker Barrel',line='Campfire Meals, and the Worst Camper in the World.',tag='Campaign · Relaunch',hero='cb-1.jpg',
  body=['After a two-year hiatus, Cracker Barrel asked us to help re-launch their Campfire Meals.',
        'So we created a humorous, fully-integrated, geo-targeted campaign featuring the Worst Camper in the World that would find our audience as they neared Cracker Barrel restaurants on their mobile devices.',
        'We also targeted past Cracker Barrel visitors as well as those near competitive locations. The video content was supported with social videos, mobile & digital banners, and a targeted email campaign.'],
  meta=[('Role','Executive Creative Director')],films=[('Watch film one',V+'177602419'),('Watch film two',V+'177250183')],gallery=['cb-2.jpg'],gclass='one'),
 dict(slug='tusk-wine',key='tusk',name='Tusk Wine',line='A new, high-end wine.',tag='Design · Packaging',hero='tusk-1.jpg',
  body=['Tusk Wine is a new, high-end wine that’s taking the luxury wine category by storm. The founders are passionate, committed and have poured their souls into the making of the wine. It took dedication and hard-work to sample enough product to bring this brand to life. That’s how committed we were.'],
  meta=[('Credits','Mark Wiegard, CD and Art Director.')],films=[],gallery=[],gclass=''),
 dict(slug='sony',key='sony',name='Sony Alpha',line='Launch of Sony’s first digital SLR.',tag='Campaign · Print',hero='sony-1.jpg',
  body=['For the launch of Sony’s first digital SLR, the goal was to highlight the dust-proof nature of the Sony’s built-in dust protection system. The launch was an incredible success and first year sales exceeded initial projections.'],
  meta=[('Role','Creative Director'),('Agency','Bagby'),('Credits','Robert Frolich, Art Director.')],films=[],gallery=['sony-2.jpg'],gclass='one'),
 dict(slug='jim-beam',key='jimbeam',name='Jim Beam Honey',line='Honey bourbon, in three headlines.',tag='Campaign · Print',hero=None,
  body=['Bourbon. Plus honey. Enough said.'],
  meta=[('Role','Creative Director'),('Agency','Proof'),('Credits','Amy Stanec, Art Director. Greg Pollack, CD.')],films=[],gallery=['jb-1.jpg','jb-2.jpg','jb-3.jpg'],gclass='three'),
 dict(slug='depaul',key=None,name='DePaul University',line='This is not a bus shelter.',tag='Campaign · Brand',hero=None,
  body=['DePaul University needed a new branding campaign.','I was happy to help.'],
  meta=[('Role','Creative Director')],films=[('Watch the film',V+'308334099')],gallery=['depaul-1.jpg','depaul-2.jpg','depaul-3.jpg'],gclass='three'),
 dict(slug='princeton',key=None,name='Princeton University',line='Venture Forward.',tag='Campaign · Brand',hero='pr-1.jpg',
  body=['Digital Pulp is a premier NY-based agency that focuses on Higher Ed. They asked me to help Princeton create a new branding and annual giving campaign for 2020.','Working with Princeton and Digital Pulp was a wonderful, collaborative process.'],
  meta=[('Agency','Digital Pulp')],films=[('Watch the film',V+'494187523')],gallery=['pr-2.jpg','pr-3.jpg','pr-4.jpg','pr-5.jpg','pr-9.jpg','pr-10.jpg','pr-6.jpg','pr-8.jpg'],gclass=''),
 dict(slug='transunion',key=None,name='TransUnion',line='A total rebrand and a new website.',tag='Brand · Digital',hero='tu-3.jpg',
  body=['TransUnion asked for a total rebrand. Working with the design agency, Avenue, I led the team that re-designed and overhauled their old school website. Working with UX, developers and content strategists, we created a thoroughly modern site with a clean and streamlined interface built for today.'],
  meta=[('Role','Creative Director'),('Agency','Digitas'),('Design partner','Avenue')],films=[],gallery=['tu-4.jpg','tu-5.jpg','tu-6.jpg','tu-1.jpg','tu-2.jpg'],gclass=''),
 dict(slug='equal',key=None,name='Equal',line='Eighty years old, with a new look.',tag='Brand · Social',hero='equal-1.jpg',
  body=['After 80 years, how do you say anything new about Equal? We took Equal back to basics and gave it a hipper more modern look for a new generation across social, digital and mobile. After all, life’s sweeter with Equal.'],
  meta=[('Scope','Social, digital and mobile')],films=[],gallery=['equal-2.jpg','equal-3.jpg','equal-oatmeal.webp','equal-wwl.webp','*equal-4.jpg'],gclass=''),
 dict(slug='samsung-facebook',key=None,name='Samsung Facebook',line='From 11,000 likes to over 11 million in a year.',tag='Digital · Social',hero='sfb-1.jpg',
  body=['Samsung has one of the fastest growing pages in Facebook’s history, skyrocketing from 11,000 likes to over 11 million in a year. Working with our tech and social teams, I led the creative team that helped build the interactive guide to their Galaxy phones. It was a site within Facebook that included real-time RSS feeds of news and videos about Galaxy phones and a 3D viewer for every model plus their features. Some of the things we did have never been done before on Facebook.'],
  meta=[('Role','Creative Director'),('Agency','Razorfish')],films=[],gallery=['sfb-2.jpg','sfb-3.jpg','sfb-4.jpg'],gclass=''),
 dict(slug='chicago-tech-plan',key=None,name='City of Chicago Tech Plan',line='The city’s first Tech Plan, for web and print.',tag='Digital · Print',hero='chi-1.jpg',
  body=['Mayor Rahm Emanuel asked Digitas to translate Chicago’s first ever Tech Plan for web and print.'],
  meta=[('Role','Creative Director'),('Agency','Digitas'),('Credits','Camilo Medina, Designer. Matthew Jacobson, Head of Design. Kristen Miller, Head of UX.')],films=[],gallery=['chi-3.jpg','chi-4.jpg','chi-5.jpg'],gclass='three'),
 dict(slug='farm-to-fork',key=None,name='Farm to Fork',line='Launching a pasta sauce that had a name and a recipe.',tag='Brand · Launch',hero='f2f-1.jpg',
  body=['Mizkan asked us to launch their new premium pasta sauce. All they had was the name, Farm to Fork, and recipe made with wholesome ingredients from sustainable family farms.',
        'The rest was up to us, including branding, tone of voice, the website, digital work as well as shooting a tomato harvest in 110 degree weather in mid-July. I think the results were pretty tasty.'],
  meta=[('Client','Mizkan')],films=[('Watch the film',V+'312604256')],gallery=['f2f-4.jpg','f2f-5.jpg','f2f-2.jpg','f2f-3.jpg'],gclass=''),
 dict(slug='coleman',key=None,name='Coleman',line='A Kelly Awards finalist.',tag='Campaign · Print',hero='col-1.jpg',
  body=['This campaign for Coleman was nominated for the Kelly awards.'],
  meta=[('Role','Associate Creative Director'),('Agency','BBDO'),('Credits','Paul Szary, Art Director.')],films=[],gallery=['col-2.jpg','col-3.jpg'],gclass=''),
 dict(slug='reel',key=None,name='The reel',line='A few highlights from a lot of shoots.',tag='Film · Broadcast',hero=None,
  body=['Just a few highlights of the many commercials I’ve shot over my career.'],
  meta=[],films=[('Watch the reel',V+'18578479')],gallery=[],gclass='',side='sf-loop.webp'),
]
ARROW='<svg class="go" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def case_html(c,i,bar):
    prev=CASES[(i-1)%len(CASES)]; nxt=CASES[(i+1)%len(CASES)]
    hero=f'<div class="hero-media"><img src="img/{c["hero"]}" alt="{c["name"]}" loading="lazy"></div>' if c.get('hero') else ''
    if c.get('hero','') and c['hero'].endswith('.mp4'):   # a silent looping clip of our own: starts when the page opens
        hero=f'<div class="hero-media"><video src="img/{c["hero"]}" poster="img/{c["hero"][:-4]}-poster.jpg" loop muted playsinline preload="none" aria-label="{c["name"]}"></video></div>'
    if c.get('film'):   # (vimeo id, width, height, label): the film plays muted on a loop as the hero. The player is only created while the page is open.
        vid,vw,vh,lab=c['film']
        hero=f'<div class="hero-media film" style="aspect-ratio:{vw}/{vh};max-width:{round(vw*1.6)}px" data-vimeo="{vid}" data-label="{lab}"></div>'
    body=''.join((f'<h3>{p[3:]}</h3>' if p.startswith('## ') else f'<p>{p}</p>') for p in c['body'])
    meta=''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k,v in c['meta'])
    films=''.join(f'<a class="cbtn li" href="{u}"><span>{t}</span>{ARROW}</a>' for t,u in c['films'])
    if c.get('link'): films+=f'<a class="cbtn mail" href="{c["link"][1]}"><span>{c["link"][0]}</span>{ARROW}</a>'
    films=f'<div class="films">{films}</div>' if films else ''
    side=f'<div class="side-media"><img src="img/{c["side"]}" alt="{c["name"]}" loading="lazy"></div>' if c.get('side') else ''
    gal=''.join(f'<img{" class=\"wide\"" if g.startswith("*") else ""} src="img/{g.lstrip("*")}" alt="{c["name"]}, image {n+1}" loading="lazy">' for n,g in enumerate(c['gallery']))  # a leading * makes an image span the full row
    gal=f'<div class="gallery {c["gclass"]}">{gal}</div>' if gal else ''
    return f'''<div id="v-{c["slug"]}" class="view sub" hidden>
{bar}
<article class="case">
  <a class="back" href="#work">← All work</a>
  <p class="kicker">{c["tag"]}</p>
  <h1 class="headline flow">{c["name"]}. <span>{c["line"]}</span></h1>
  {hero}
  <div class="cols"><div class="body">{body}</div><aside class="meta"><dl>{meta}</dl>{films}{side}</aside></div>
  {gal}
  <nav class="pager" aria-label="More work"><a href="#{prev["slug"]}"><small>Previous</small>{prev["name"]}</a><a class="nx" href="#{nxt["slug"]}"><small>Next</small>{nxt["name"]}</a></nav>
</article>
</div>'''
SLUG={c['key']:c['slug'] for c in CASES if c['key']}
