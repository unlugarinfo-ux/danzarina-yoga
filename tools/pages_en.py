# English pages (run by build.py with L = 'en'), British spelling.
# Faithful translation of the French version: add no information that is not in the French.

def crumbs(name, key):
    return [{'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE['url'] + u('accueil')},
        {'@type': 'ListItem', 'position': 2, 'name': name, 'item': SITE['url'] + u(key)}]}]

# ---------- HOME ----------
pages.append(page(u('accueil'),
 'Dance & Yoga in Saint-Joseph, Réunion Island | Danzarina',
 'Dance and yoga classes, workshops, private sessions and experiences for hotels in Saint-Joseph and the south of Réunion Island.',
f'''<section class="hero-t" aria-labelledby="h1-accueil">
<figure class="hero-t__media">{picture('accueil-julieta-voile-terracotta', 'Julieta balancing on one leg, arm raised, holding a terracotta and olive veil; a large terracotta silk cloth unfolds beside her.', '100vw', eager=True, mobile=('accueil-julieta-voile-terracotta-4x5', '(max-width: 47.99rem)'))}<figcaption>Artistic image</figcaption></figure>
<div class="wrap hero-t__grille"><div class="hero-t__texte">
<p class="eyebrow">Saint-Joseph · South of Réunion Island</p>
<h1 id="h1-accueil"><span class="hero-t__l1">Dance &amp; Yoga</span> <span class="hero-t__l2">in Saint-Joseph, Réunion Island</span></h1>
<p class="lead">Dance and yoga classes, workshops and private sessions. A harmonious rhythm between dance and yoga, to inhabit your body with grace and fluidity.</p>
<div class="actions"><a class="btn btn--clair" href="{u('yoga')}">Discover yoga</a><a class="btn btn--ligne" href="{u('danse')}">Discover dance</a></div>
</div></div></section>''',
 f'''<section class="manifeste" aria-label="Our intention"><div class="wrap">
<p class="manifeste__mots"><span>Breathe</span> <span>Recentre</span> <span>Connect</span></p>
<p class="manifeste__texte">Classes for all ages and all levels, respecting each person’s pace.</p>
</div></section>

<section class="section section--sable" aria-labelledby="offre-titre"><div class="wrap">
<div class="entete-section"><p class="eyebrow">What we offer</p><h2 id="offre-titre">Move, breathe, connect</h2></div>
<ol class="offres">
<li class="offre"><span class="offre__num" aria-hidden="true">01</span><h3>Dance</h3><p>Tango, salsa and dance for children: dancing for the joy of movement and of meeting others.</p><a class="lien-fleche" href="{u('danse')}">Dance classes</a></li>
<li class="offre"><span class="offre__num" aria-hidden="true">02</span><h3>Yoga</h3><p>Shantyoga, a yoga that adapts to each student and focuses on alignment.</p><a class="lien-fleche" href="{u('yoga')}">Yoga classes</a></li>
<li class="offre"><span class="offre__num" aria-hidden="true">03</span><h3>Private lessons</h3><p>A session built around your goal, at your own pace.</p><a class="lien-fleche" href="{u('perso')}">How it works</a></li>
</ol>
</div></section>

<section class="section section--olive" aria-labelledby="plage-titre"><div class="wrap duo">
<div>
<p class="eyebrow">This week</p>
<h2 id="plage-titre">Beach yoga on Tuesday mornings</h2>
<p class="lead">Shantyoga adapts to each student and places strong emphasis on alignment: listening to the body, breathing, alignment, presence and well-being.</p>
<a class="lien-fleche" href="{u('yoga')}">All about yoga</a>
</div>
{yoga_plage()}
</div></section>

<figure class="bandeau bandeau--x">
{picture('danse-canape-ciel-2x1', 'A dancer supports a dancer in full extension above an antique sofa standing in a meadow, in front of a hay bale and mountains at sunset.', '100vw', mobile=('danse-canape-ciel-4x5', '(max-width: 35.99rem)'))}
<figcaption class="bandeau__phrase">“The body opens a space”</figcaption>
</figure>

<section class="section" aria-labelledby="parcours-titre"><div class="wrap duo duo--inverse">
<figure class="cadre-decale">{picture('parcours-noir-et-blanc', 'Black and white photo: a dancer standing on an antique sofa in a field, a man sitting beside her, mountains in the distance.', '(min-width: 56rem) 50vw, 100vw')}<figcaption>Danzarina archive.</figcaption></figure>
<div>
<p class="eyebrow">A journey in movement</p>
<h2 id="parcours-titre">A life of dancing and teaching</h2>
<p>Danzarina grew out of the journey of Julieta, a movement artist from Argentina with over 20 years’ training in ballet, jazz, contemporary dance, tango, Argentine folk dance, salsa, zouk and kizomba. Today she combines dance and yoga in her own teaching method.</p>
<p>Today, Danzarina continues its path in Réunion Island.</p>
<a class="lien-fleche" href="{u('apropos')}">Discover our story</a>
</div>
</div></section>

<section class="section section--sable" aria-label="Going further"><div class="wrap tuiles">
<article class="tuile tuile--terre"><p class="eyebrow">Professionals</p><h2 class="tuile__titre">Hotels &amp; partners</h2><p>Dance or yoga sessions at your venue, adapted to your space and your guests.</p><a class="btn btn--clair" href="{u('hotels')}">Tell us about your project</a></article>
<article class="tuile tuile--olive"><p class="eyebrow">One-off sessions</p><h2 class="tuile__titre">Workshops</h2><p>Workshops to deepen a practice. Upcoming dates will be announced here and on Instagram.</p><a class="btn btn--clair" href="{u('ateliers')}">See the workshops</a></article>
</div></section>
{contact_cta(sur_sable=True)}''',
 schema=[{'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Danzarina', 'url': SITE['url'] + u('accueil'), 'inLanguage': 'en'}]))

# ---------- DANCE ----------
pages.append(page(u('danse'),
 'Dance classes in Saint-Joseph, Réunion Island: tango, salsa, children | Danzarina',
 'Dance classes with Danzarina in the south of Réunion Island: tango and salsa for adults, dance for children. Practise at your own pace, without pressure.',
 titre('Dance', 'Dance classes', 'Dancing for the joy of movement, music and meeting others, at your own pace and with no competitive spirit.'),
 f'''<section class="section" style="padding-top:0"><div class="wrap">
{picture('hero-danse-a-deux-16x9', 'A couple dancing together in a meadow, in orange T-shirts, in the late-afternoon sun.', '(min-width: 72rem) 68rem, 100vw', cls='', mobile=('hero-danse-a-deux-4x5', '(max-width: 35.99rem)'))}
</div></section>
<section class="section" style="padding-top:0" aria-labelledby="styles-titre"><div class="wrap">
<h2 id="styles-titre">The dances we teach</h2>
<div class="grille grille--3">
<article class="carte"><h3>Tango</h3><p>For adults. A dance of listening and connection, where you learn to walk together.</p></article>
<article class="carte"><h3>Salsa</h3><p>For adults. A joyful, rhythmic dance to let go and share.</p></article>
<article class="carte"><h3>Dance for children</h3><p>An introduction to and discovery of movement, music and expression.</p></article>
</div>
</div></section>
{vague()}
<section class="section section--sable" aria-labelledby="methode-titre"><div class="wrap duo">
<div>
<h2 id="methode-titre">How we teach</h2>
<ul class="liste-points">
<li>Open to everyone, beginners and experienced dancers alike.</li>
<li>Everyone progresses at their own pace: there is no performance to reach.</li>
<li>On your own or as a couple: you do not need to bring a partner.</li>
<li>Attention to listening to the body and to connection.</li>
</ul>
<h3 id="horaires">Times, places and prices</h3>
<p>The times and places of the dance classes for the new season will be published here soon. In the meantime, <a href="{u('contact')}">get in touch</a> to stay informed.</p>
</div>
<figure>{picture('danse-fleurs-violettes', 'Two dancers face each other mid-figure in a partner dance, among purple flowers, under a blue sky.', '(min-width: 56rem) 50vw, 100vw')}</figure>
</div></section>
{vague(' vague--haut')}
<section class="section" aria-labelledby="galerie-titre"><div class="wrap">
<h2 id="galerie-titre">In motion</h2>
<ul class="galerie">
<li>{picture('danse-canape-paysage', 'A dancer supports a dancer in full extension above an antique sofa on the grass, with mountains behind.', '(min-width: 60rem) 33vw, 100vw')}</li>
<li>{picture('mouvement-sous-le-ciel-4x5', 'Two dancers in full flight in a field, under a cloudy sky.', '(min-width: 60rem) 33vw, 100vw')}</li>
<li>{picture('parcours-noir-et-blanc', 'Black and white photo of two dancers around an antique sofa in a field.', '(min-width: 60rem) 33vw, 100vw')}</li>
</ul>
</div></section>
{contact_cta('Feel like dancing?', 'Tell us what draws you and we will guide you towards the class that suits you.')}''',
 schema=crumbs('Dance', 'danse')))

# ---------- YOGA ----------
pages.append(page(u('yoga'),
 'Yoga classes in Saint-Joseph: Shantyoga on Grand Anse beach | Danzarina',
 'Shantyoga classes in Saint-Joseph, Réunion Island: beach yoga at Grand Anse on Tuesdays from 9.30 to 11 am. A yoga that adapts to each student.',
 titre('Yoga', 'Yoga classes in Saint-Joseph', 'Shantyoga: a style of yoga that adapts to each student and places strong emphasis on alignment.'),
 f'''<section class="section" style="padding-top:0"><div class="wrap duo">
<div>
<h2>Our approach</h2>
<p>Each session leaves time to arrive, breathe and listen to your body. The postures are adapted to each person: what matters is not how far you go, but being in the right place.</p>
<ul class="liste-points">
<li>Listening to the body</li><li>Breathing</li><li>Alignment</li><li>Presence</li><li>Well-being</li>
</ul>
</div>
{yoga_plage()}
</div></section>
<figure class="bandeau bandeau--doux">{picture('ambiance-yoga-tapis', '', '100vw')}</figure>
{vague()}
<section class="section section--sable" aria-labelledby="pratique-titre"><div class="wrap">
<h2 id="pratique-titre">Practical information</h2>
<div class="grille grille--3">
<article class="carte"><h3>Level</h3><p>Open to everyone, whatever your age or level.</p></article>
<article class="carte"><h3>What to bring</h3><p>Comfortable clothes. For the mat and anything else, <a href="{u('contact')}">ask us</a> before your first session.</p></article>
<article class="carte"><h3>Health</h3><p>Yoga is no substitute for medical advice. If you are pregnant, injured or have a health condition, talk to your doctor and let us know before the session.</p></article>
</div>
</div></section>
{vague(' vague--haut')}
<section class="section" aria-labelledby="enseignante-titre"><div class="wrap">
<h2 id="enseignante-titre">The teacher</h2>
<p>Julieta holds a 200-hour Shantyoga certification (2019, training recognised by Yoga Alliance) and is training in Iyengar yoga.</p>
<a class="lien-fleche" href="{u('apropos')}">More about Julieta</a>
</div></section>
{contact_cta('Would you like to try?', 'Write to us to find out about the next sessions and book your place.')}''',
 schema=crumbs('Yoga', 'yoga')))

# ---------- PRIVATE LESSONS ----------
pages.append(page(u('perso'),
 'Private dance and yoga lessons in Saint-Joseph | Danzarina',
 'Private dance or yoga sessions in the south of Réunion Island: a conversation, a goal, a tailored format and follow-up.',
 titre('Private lessons', 'Private dance and yoga lessons', 'A session designed for you: on your own, as a couple or in a small group, around a goal that suits you.'),
 f'''<section class="section" style="padding-top:0" aria-labelledby="etapes-titre"><div class="wrap">
<h2 id="etapes-titre">How it works</h2>
<ol class="etapes">
<li><h3>A first conversation</h3><p>You tell us about yourself, what you would like and any constraints you may have.</p></li>
<li><h3>Your goal</h3><p>Opening the dance at a wedding, getting moving again, deepening a practice…</p></li>
<li><h3>A proposal</h3><p>We suggest a format: length, number of sessions, dance or yoga.</p></li>
<li><h3>The session</h3><p>Time at your own pace, focused on you.</p></li>
<li><h3>Follow-up</h3><p>We review together and adjust what comes next.</p></li>
</ol>
</div></section>
{vague()}
<section class="section section--sable"><div class="wrap">
<h2>Place and arrangements</h2>
<p>Possible venues, prices and travel arrangements are set out during the first conversation.</p>
</div></section>
{contact_cta('Let’s talk about your project', 'Describe what you have in mind in a few lines: we will get back to you to discuss it.', 'Request a session', sur_sable=True)}'''))

# ---------- WORKSHOPS ----------
pages.append(page(u('ateliers'),
 'Dance and yoga workshops in Saint-Joseph, Réunion Island | Danzarina',
 'Danzarina dance and yoga workshops in the south of Réunion Island: dates, places and bookings.',
 titre('Workshops', 'Dance and yoga workshops', 'One-off sessions to deepen a practice, discover a dance or take some time for yourself.'),
 f'''<section class="section" style="padding-top:0"><div class="wrap">
<div class="encart">
<h2 style="font-size:1.4rem">Upcoming workshops</h2>
<p>No workshop is scheduled at the moment. Upcoming dates will be announced on this page and on <a href="{SITE['instagram']}" rel="noopener">Instagram</a>.</p>
<p style="margin:0">Would you like to be told? <a href="{u('contact')}">Write to us</a>.</p>
</div>
</div></section>
{contact_cta()}'''))

# ---------- HOTELS ----------
pages.append(page(u('hotels'),
 'Dance and yoga for hotels and accommodation in Réunion Island | Danzarina',
 'Yoga and dance sessions for hotels, guesthouses and accommodation in the south of Réunion Island: flexible formats, on-site sessions, a quote based on your project.',
 titre('Hotels & partners', 'Dance and yoga for hotels and accommodation', 'A well-being and movement offer for your guests, built with you around your venue.'),
 f'''<section class="section" style="padding-top:0" aria-labelledby="formats-titre"><div class="wrap">
<h2 id="formats-titre">What we can build together</h2>
<div class="grille grille--2">
<article class="carte"><h3>Flexible formats</h3><p>Yoga, dance or an introduction, as a one-off or regular session, to suit the rhythm of your venue.</p></article>
<article class="carte"><h3>At your venue</h3><p>We come to your venue, indoors or outdoors depending on the spaces available.</p></article>
<article class="carte"><h3>Tailored to your guests</h3><p>A proposal designed around the number of participants, their expectations and the setting.</p></article>
<article class="carte"><h3>A clear quote</h3><p>After a first conversation, we send you a detailed proposal.</p></article>
</div>
</div></section>
<figure class="bandeau bandeau--doux">{picture('ambiance-frangipanier', '', '100vw')}</figure>
{vague()}
<section class="section section--sable" aria-labelledby="infos-titre"><div class="wrap">
<h2 id="infos-titre">To prepare your request</h2>
<ul class="liste-points">
<li>The name and location of your venue</li>
<li>The type of session you are interested in (yoga, dance, both)</li>
<li>The expected number of participants</li>
<li>The spaces available and the dates you have in mind</li>
</ul>
</div></section>
{contact_cta('Tell us about your project', 'Introduce your venue and what you would like: we will get back to you quickly.', 'Tell us about your project', sur_sable=True)}'''))

# ---------- ABOUT ----------
pages.append(page(u('apropos'),
 'About Danzarina: Julieta, dance and yoga in Réunion Island | Danzarina',
 'The story of Danzarina and Julieta, a movement artist from Argentina: dance, Shantyoga and a new chapter in Réunion Island.',
 titre('About', 'About Danzarina', 'A harmonious rhythm between dance and yoga, to enrich life with grace and fluidity.'),
 f'''<section class="section" style="padding-top:0" aria-labelledby="julieta-titre"><div class="wrap duo">
<figure>{picture('portrait-editorial-julieta', 'Artistic portrait of Julieta walking barefoot along a path, in a long skirt and layered veils, at sunset.', '(min-width: 56rem) 50vw, 100vw')}<figcaption>Artistic portrait.</figcaption></figure>
<div>
<p class="eyebrow">The founder</p>
<h2 id="julieta-titre">Julieta</h2>
<h3>Her story</h3>
<p>A movement artist from Argentina, Julieta has been training in dance for over 20 years. A dancer of ballet, jazz, contemporary dance, tango, Argentine folk dance, salsa, zouk and kizomba, she has specialised in each of these styles.</p>
<p>She has had a long journey in dance and around the world, sharing her expertise in various cities and dance schools across Slovakia, Spain and France.</p>
<h3>Her training</h3>
<ul class="liste-points">
<li>Over 20 years’ training in dance: ballet, jazz, contemporary dance, tango, Argentine folk dance, salsa, zouk and kizomba, among others</li>
<li>Training with renowned artists and teachers in Slovakia, Argentina (Córdoba, Buenos Aires), Spain and France</li>
<li>200-hour Shantyoga certification (2019), training recognised by Yoga Alliance</li>
<li>Currently taking Iyengar yoga courses</li>
</ul>
<h3>Her path in yoga</h3>
<p>Today she continues her path in yoga, creating her own teaching system in which she applies everything she has learnt over a life devoted to movement. She teaches dance to children, tango and salsa to adults, and yoga.</p>
</div>
</div></section>
{vague()}
<section class="section section--sable" aria-labelledby="parcours-titre"><div class="wrap duo duo--inverse">
<figure>{picture('danse-canape-paysage', 'A dancer supports a dancer in full extension above an antique sofa on the grass, with mountains behind.', '(min-width: 56rem) 50vw, 100vw')}<figcaption>Danzarina archive.</figcaption></figure>
<div>
<p class="eyebrow">A journey in movement</p>
<h2 id="parcours-titre">Dancing as a couple</h2>
<p>Julieta shares dance with Christian, a teacher and dancer, with whom she dances tango and salsa. Christian learnt African dance with Hamed.</p>
</div>
</div></section>
{vague(' vague--haut')}
<section class="section" aria-labelledby="vision-titre"><div class="wrap">
<p class="eyebrow">Danzarina’s vision</p>
<h2 id="vision-titre">One land, the same movement</h2>
<p>Simplicity, nature, peace and fraternity: Danzarina wants to offer a space where everyone can move, breathe and connect, whatever their age or level. After a journey in movement, Danzarina now continues its work in Saint-Joseph, in the south of Réunion Island.</p>
</div></section>
{contact_cta()}''',
 schema=[{'@context': 'https://schema.org', '@type': 'Person', 'name': 'Julieta', 'jobTitle': 'Dance and yoga teacher', 'worksFor': {'@id': SITE['url'] + '/#organisation'}}]))

# ---------- CONTACT ----------
pages.append(page(u('contact'),
 'Contact | Danzarina, dance and yoga in Saint-Joseph',
 'Contact Danzarina about dance and yoga classes in Saint-Joseph and the south of Réunion Island: phone, email, form.',
 titre('Contact', 'Contact', f'A question about the classes, a project for your venue? We work in {T("zone")}.'),
 f'''<section class="section" style="padding-top:0"><div class="wrap duo" style="align-items:start">
<div>
<h2>Get in touch</h2>
<ul class="coord">
<li>Phone: <a href="tel:{SITE['tel_lien']}">&nbsp;+262 6 93 77 78 75</a></li>
<li>Email: <a href="mailto:{SITE['email']}">&nbsp;{SITE['email']}</a></li>
<li>Instagram: <a href="{SITE['instagram']}" rel="noopener">&nbsp;{SITE['instagram_nom']}</a></li>
<li>Facebook: <a href="{SITE['facebook']}" rel="noopener">&nbsp;Danzarina France</a></li>
</ul>
<h2 style="margin-top:2.5rem">Frequently asked questions</h2>
<div class="faq">
<details><summary>Do I need any previous experience?</summary><p>No. The classes are open to everyone, whatever their level.</p></details>
<details><summary>Do I need to bring a partner to dance?</summary><p>No, you can come on your own.</p></details>
<details><summary>Where do the yoga classes take place?</summary><p>Beach yoga takes place at Grand Anse, in Saint-Joseph, on Tuesdays from 9.30 to 11 am.</p></details>
</div>
</div>
<div>
<h2>Send a message</h2>
<form class="form" name="contact" method="POST" action="{u('merci')}" data-netlify="true" netlify-honeypot="site-web" data-valider data-email="{T('email_inv')}" data-requis="{T('requis')}">
<input type="hidden" name="form-name" value="contact">
<input type="hidden" name="langue" value="en">
<p class="cache"><label>Do not fill in: <input name="site-web" tabindex="-1" autocomplete="off"></label></p>
<p class="mention" style="margin:0">Fields marked with an asterisk (*) are required.</p>
<div class="champ"><label for="nom">Full name *</label><input id="nom" name="nom" type="text" autocomplete="name" required aria-describedby="nom-erreur" data-vide="Enter your name."><span class="erreur" id="nom-erreur" aria-live="polite"></span></div>
<div class="champ"><label for="email">Email *</label><input id="email" name="email" type="email" autocomplete="email" required aria-describedby="email-erreur" data-vide="Enter your email address."><span class="erreur" id="email-erreur" aria-live="polite"></span></div>
<div class="champ"><label for="tel">Phone</label><span class="aide" id="tel-aide">Optional, if you would rather we called you.</span><input id="tel" name="telephone" type="tel" autocomplete="tel" aria-describedby="tel-aide"></div>
<div class="champ"><label for="sujet">Your enquiry is about</label><select id="sujet" name="sujet"><option>Dance</option><option>Yoga</option><option>Private lessons</option><option>Workshops</option><option>Hotels &amp; partners</option><option>Other</option></select></div>
<div class="champ"><label for="message">Message *</label><textarea id="message" name="message" required aria-describedby="message-erreur" data-vide="Write your message."></textarea><span class="erreur" id="message-erreur" aria-live="polite"></span></div>
<p class="mention">Your details are used only to reply to your enquiry. See our <a href="{u('confidentialite')}">privacy policy</a>.</p>
<button class="btn btn--plein" type="submit">Send message</button>
</form>
</div>
</div></section>''',
 schema=[{'@context': 'https://schema.org', '@type': 'ContactPage', 'name': 'Contact Danzarina', 'url': SITE['url'] + u('contact')}]))

# ---------- THANK YOU ----------
pages.append(page(u('merci'), 'Message sent | Danzarina', 'Your message has been sent to Danzarina.',
 titre('Thank you', 'Message sent', 'Thank you for your message. We will reply as soon as possible.'),
 f'<section class="section" style="padding-top:0"><div class="wrap"><a class="btn btn--plein" href="{u("accueil")}">Back to home</a></div></section>', robots='noindex, follow'))

# ---------- LEGAL ----------
AV = '<p class="mention">Translation for information only. In case of any difference, the French version prevails.</p>'
pages.append(page(u('mentions'), 'Legal notice | Danzarina', 'Legal notice for the danzarina.fr website.',
 titre('Legal information', 'Legal notice', 'In accordance with French law no. 2004-575 of 21 June 2004 on confidence in the digital economy (LCEN).'),
 f'''<section class="section contenu-legal" style="padding-top:0"><div class="wrap">
{AV}
<h2>Website publisher</h2>
<p>{SITE['nom_long']}, association {AC}<br>Registered office: {AC}<br>RNA number: {AC} · SIRET (if applicable): {AC}<br>Phone: {SITE['tel_affiche']} · Email: <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
<h2>Publication director</h2>
<p>{AC}</p>
<h2>Hosting</h2>
<p>Netlify, Inc., 512 2nd Street, Suite 200, San Francisco, CA 94107, United States · <a href="https://www.netlify.com" rel="noopener">www.netlify.com</a></p>
<h2>Intellectual property</h2>
<p>All content on this website (texts, photographs, logo) belongs to Danzarina or to its authors. Any reproduction without permission is prohibited. The people photographed have agreed to the publication of their image.</p>
<h2>Credits</h2>
<p>Photographs: {AC}. The portrait on the About page is an artistic image.</p>
</div></section>''', robots='noindex, follow'))

pages.append(page(u('confidentialite'), 'Privacy policy | Danzarina', 'Privacy and personal data protection policy for the danzarina.fr website.',
 titre('Personal data', 'Privacy policy', 'How we handle the data you share with us, in accordance with the GDPR and the French Data Protection Act.'),
 f'''<section class="section contenu-legal" style="padding-top:0"><div class="wrap">
{AV}
<h2>Data controller</h2>
<p>{SITE['nom_long']}, {AC} · <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
<h2>Data collected</h2>
<p>Through the contact form: name, email address, phone number (optional), subject and content of your message. No other data is collected.</p>
<h2>Purpose and legal basis</h2>
<p>To reply to your enquiry (legitimate interest, or pre-contractual steps if you ask for a quote).</p>
<h2>Recipients</h2>
<p>Only the Danzarina team. Messages pass through our host, Netlify (Netlify Forms service), based in the United States and covered by the European Commission’s standard contractual clauses.</p>
<h2>Retention period</h2>
<p>Three years from our last exchange, after which they are deleted.</p>
<h2>Cookies and analytics</h2>
<p>This website uses no analytics or advertising cookies and no third-party tracking services. The fonts are hosted on our own server.</p>
<h2>Your rights</h2>
<p>You have the right of access, rectification, erasure, restriction, objection and portability. To exercise them: <a href="mailto:{SITE['email']}">{SITE['email']}</a>. You may also lodge a complaint with the CNIL (<a href="https://www.cnil.fr" rel="noopener">www.cnil.fr</a>).</p>
<p class="mention">Last updated: {AC}</p>
</div></section>''', robots='noindex, follow'))
