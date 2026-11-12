#!/usr/bin/env python3
"""Génère les pages HTML statiques de danzarina.fr.
Usage : python3 tools/build.py   (depuis la racine du dépôt)
Les données à confirmer sont regroupées dans SITE et marquées « À COMPLÉTER ».
"""
import json, os, html
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = json.load(open(os.path.join(ROOT, 'assets/images/optimized/manifest.json')))
TODAY = date.today().isoformat()

SITE = {
    'url': 'https://danzarina.fr',
    'nom': 'Danzarina',
    'nom_long': 'Association Danzarina · Danse & Yoga',
    'tel_affiche': '06 93 77 78 75',
    'tel_lien': '+262693777875',
    'email': 'assodanzarina@gmail.com',
    'instagram': 'https://www.instagram.com/danzarina_association/',
    'instagram_nom': '@danzarina_association',
    'facebook': 'https://www.facebook.com/danzarinafrance/',
    'zone': 'Saint-Joseph et le Sud de La Réunion',
}

NAV = ['danse', 'yoga', 'perso', 'ateliers', 'hotels', 'apropos']

def esc(s): return html.escape(s, quote=True)

# ---------- Multilingue : français (racine), espagnol (/es/), anglais (/en/) ----------
L = 'fr'
LANGS = ('fr', 'es', 'en')
PATHS = {
    'accueil': {'fr': '/', 'es': '/es/', 'en': '/en/'},
    'danse': {'fr': '/danse/', 'es': '/es/danza/', 'en': '/en/dance/'},
    'yoga': {'fr': '/yoga/', 'es': '/es/yoga/', 'en': '/en/yoga/'},
    'perso': {'fr': '/cours-personnalises/', 'es': '/es/clases-personalizadas/', 'en': '/en/private-lessons/'},
    'ateliers': {'fr': '/ateliers/', 'es': '/es/talleres/', 'en': '/en/workshops/'},
    'hotels': {'fr': '/hotels-partenaires/', 'es': '/es/hoteles-colaboradores/', 'en': '/en/hotels-partners/'},
    'apropos': {'fr': '/a-propos/', 'es': '/es/sobre-nosotros/', 'en': '/en/about/'},
    'contact': {'fr': '/contact/', 'es': '/es/contacto/', 'en': '/en/contact/'},
    'merci': {'fr': '/merci/', 'es': '/es/gracias/', 'en': '/en/thank-you/'},
    'mentions': {'fr': '/mentions-legales/', 'es': '/es/aviso-legal/', 'en': '/en/legal-notice/'},
    'confidentialite': {'fr': '/politique-de-confidentialite/', 'es': '/es/politica-de-privacidad/', 'en': '/en/privacy-policy/'},
}
def u(key, lang=None): return PATHS[key][lang or L]
def cle(path):
    for k, v in PATHS.items():
        if path in v.values(): return k
    return None

CH = {
 'fr': {'menu':'Menu','lang': 'fr', 'locale': 'fr_FR', 'nom': 'Français', 'court': 'FR',
        'nav': {'danse': 'Danse', 'yoga': 'Yoga', 'perso': 'Cours personnalisés', 'ateliers': 'Ateliers', 'hotels': 'Hôtels & partenaires', 'apropos': 'À propos', 'contact': 'Contact', 'accueil': 'Accueil'},
        'skip': 'Aller au contenu', 'marque': 'Danzarina, danse et yoga : accueil', 'sous_marque': 'Danse &amp; Yoga', 'nav_label': 'Navigation principale', 'langues': 'Langue du site',
        'pied_txt': 'Cours de danse et de yoga, ateliers et séances personnalisées.', 'zone_t': 'Zone d’activité', 'zone': 'Saint-Joseph et le Sud de La Réunion',
        'mentions': 'Mentions légales', 'confid': 'Politique de confidentialité', 'logo_alt': 'Logo Danzarina',
        'cta_t': 'Une question, une envie ?', 'cta_x': 'Écrivez-nous ou appelez-nous : nous vous répondons avec plaisir.', 'cta_b': 'Nous contacter', 'appeler': 'Appeler le',
        'yp_t': 'Yoga à la plage · Grand Anse', 'yp_lieu': 'Lieu', 'yp_lieu_v': 'Plage de Grand Anse, Saint-Joseph', 'yp_jour': 'Jour', 'yp_jour_v': 'Le mardi', 'yp_h': 'Horaire', 'yp_h_v': 'De 9h30 à 11h', 'yp_style': 'Style',
        'yp_note': 'Pour connaître la reprise, les tarifs et le matériel à prévoir, <a href="{c}">contactez-nous</a>.',
        'email_inv': 'Indiquez une adresse e-mail valide, par exemple nom@exemple.fr.', 'requis': 'Ce champ est obligatoire.'},
 'es': {'menu':'Menú','lang': 'es', 'locale': 'es_ES', 'nom': 'Español', 'court': 'ES',
        'nav': {'danse': 'Danza', 'yoga': 'Yoga', 'perso': 'Clases personalizadas', 'ateliers': 'Talleres', 'hotels': 'Hoteles', 'apropos': 'Quiénes somos', 'contact': 'Contacto', 'accueil': 'Inicio'},
        'skip': 'Ir al contenido', 'marque': 'Danzarina, danza y yoga: inicio', 'sous_marque': 'Danza y Yoga', 'nav_label': 'Navegación principal', 'langues': 'Idioma de la web',
        'pied_txt': 'Clases de danza y de yoga, talleres y sesiones personalizadas.', 'zone_t': 'Zona de actividad', 'zone': 'Saint-Joseph y el sur de La Reunión',
        'mentions': 'Aviso legal', 'confid': 'Política de privacidad', 'logo_alt': 'Logotipo de Danzarina',
        'cta_t': '¿Una pregunta, unas ganas?', 'cta_x': 'Escríbenos o llámanos: te respondemos con gusto.', 'cta_b': 'Contactarnos', 'appeler': 'Llamar al',
        'yp_t': 'Yoga en la playa · Grand Anse', 'yp_lieu': 'Lugar', 'yp_lieu_v': 'Playa de Grand Anse, Saint-Joseph', 'yp_jour': 'Día', 'yp_jour_v': 'Los martes', 'yp_h': 'Horario', 'yp_h_v': 'De 9:30 a 11:00', 'yp_style': 'Estilo',
        'yp_note': 'Para saber la fecha de reanudación, las tarifas y el material necesario, <a href="{c}">contáctanos</a>.',
        'email_inv': 'Escribe un email válido, por ejemplo nombre@ejemplo.com.', 'requis': 'Este campo es obligatorio.'},
 'en': {'menu':'Menu','lang': 'en', 'locale': 'en_GB', 'nom': 'English', 'court': 'EN',
        'nav': {'danse': 'Dance', 'yoga': 'Yoga', 'perso': 'Private lessons', 'ateliers': 'Workshops', 'hotels': 'Hotels & partners', 'apropos': 'About', 'contact': 'Contact', 'accueil': 'Home'},
        'skip': 'Skip to content', 'marque': 'Danzarina, dance and yoga: home', 'sous_marque': 'Dance &amp; Yoga', 'nav_label': 'Main navigation', 'langues': 'Site language',
        'pied_txt': 'Dance and yoga classes, workshops and private sessions.', 'zone_t': 'Where we work', 'zone': 'Saint-Joseph and the south of Réunion Island',
        'mentions': 'Legal notice', 'confid': 'Privacy policy', 'logo_alt': 'Danzarina logo',
        'cta_t': 'A question, an idea?', 'cta_x': 'Write to us or give us a call: we will be glad to reply.', 'cta_b': 'Contact us', 'appeler': 'Call',
        'yp_t': 'Beach yoga · Grand Anse', 'yp_lieu': 'Place', 'yp_lieu_v': 'Grand Anse beach, Saint-Joseph', 'yp_jour': 'Day', 'yp_jour_v': 'Tuesdays', 'yp_h': 'Time', 'yp_h_v': '9.30 to 11 am', 'yp_style': 'Style',
        'yp_note': 'To find out when classes restart, prices and what to bring, <a href="{c}">get in touch</a>.',
        'email_inv': 'Enter a valid email address, for example name@example.com.', 'requis': 'This field is required.'},
}
def T(k): return CH[L][k]

def picture(name, alt, sizes, cls='', eager=False, mobile=None):
    """<picture> AVIF/WebP/JPEG avec srcset ; mobile = (nom, media) pour un recadrage alternatif."""
    m = MANIFEST[name]; w0, h0 = m['ratio']; ws = m['widths']
    def srcset(n, ext): return ', '.join(f'/assets/images/optimized/{n}-{w}.{ext} {w}w' for w in MANIFEST[n]['widths'])
    out = ['<picture>']
    if mobile:
        mn, media = mobile
        for ext, t in (('avif', 'image/avif'), ('webp', 'image/webp')):
            out.append(f'<source media="{media}" type="{t}" srcset="{srcset(mn, ext)}" sizes="100vw">')
    for ext, t in (('avif', 'image/avif'), ('webp', 'image/webp')):
        out.append(f'<source type="{t}" srcset="{srcset(name, ext)}" sizes="{sizes}">')
    load = 'fetchpriority="high" loading="eager"' if eager else 'loading="lazy"'
    w = ws[-1]; h = round(h0 * w / w0)
    out.append(f'<img src="/assets/images/optimized/{name}-{w}.jpg" srcset="{srcset(name, "jpg")}" sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt)}" decoding="async" {load}{" class=" + chr(34) + cls + chr(34) if cls else ""}>')
    out.append('</picture>')
    return ''.join(out)

VAGUE = '<svg class="vague{cls}" viewBox="0 0 1440 48" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path fill="currentColor" d="M0 30c120-18 240-24 360-12s240 30 360 18 240-36 360-30 240 24 360 18V48H0z"/></svg>'
def vague(cls=''): return VAGUE.replace('{cls}', cls)

ICONES = {
    'danse': '<svg class="carte__icone" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="26" cy="8" r="4"/><path d="M24 14l-4 12 8 6-2 12M20 26l-8 4M24 14l10 6 6-6"/></svg>',
    'yoga': '<svg class="carte__icone" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="24" cy="9" r="4"/><path d="M24 15v13M14 4l10 11 10-11M10 38c6-6 22-6 28 0M16 34l8-6 8 6"/></svg>',
    'perso': '<svg class="carte__icone" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="17" cy="14" r="5"/><circle cx="33" cy="18" r="4"/><path d="M8 40c0-8 4-14 9-14s9 6 9 14M27 40c0-6 3-11 6-11s7 5 7 11"/></svg>',
    'hotel': '<svg class="carte__icone" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 40h36M10 40V14l14-8 14 8v26M19 40v-9h10v9M17 20h4M27 20h4"/></svg>',
}

def selecteur(path):
    k = cle(path)
    out = []
    for lg in LANGS:
        href = u(k, lg) if k else u('accueil', lg)
        cur = ' aria-current="true"' if lg == L else ''
        out.append(f'<li><a href="{href}" hreflang="{lg}" lang="{lg}"{cur}><abbr title="{CH[lg]["nom"]}">{CH[lg]["court"]}</abbr></a></li>')
    return f'<ul class="langues" aria-label="{T("langues")}">{"".join(out)}</ul>'

def entete(actif):
    items = []
    for k in NAV:
        href = u(k); cur = ' aria-current="page"' if href == actif else ''
        items.append(f'<li><a href="{href}"{cur}>{esc(T("nav")[k])}</a></li>')
    cur = ' aria-current="page"' if actif == u('contact') else ''
    items.append(f'<li><a class="nav-cta" href="{u("contact")}"{cur}>{T("nav")["contact"]}</a></li>')
    return f'''<a class="skip" href="#contenu">{T('skip')}</a>
<header class="entete">
  <div class="wrap">
    <a class="marque" href="{u('accueil')}" aria-label="{T('marque')}">
      <img src="/assets/brand/logo-cercle-128.webp" width="128" height="128" alt="">
      <span>Danzarina<small>{T('sous_marque')}</small></span>
    </a>
    {selecteur(actif)}
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>{T("menu")}
    </button>
    <nav id="nav" class="nav" aria-label="{T('nav_label')}"><ul>{''.join(items)}</ul>{selecteur(actif).replace('class="langues"', 'class="langues langues--menu"')}</nav>
  </div>
</header>'''

def pied():
    nav = ''.join(f'<li><a href="{u(k)}">{esc(T("nav")[k])}</a></li>' for k in ['accueil'] + NAV + ['contact'])
    return f'''<footer class="pied">
  <div class="wrap">
    <div class="pied__grille">
      <div>
        <img class="pied__logo" src="/assets/brand/logo-cercle-256.webp" width="256" height="256" alt="{T('logo_alt')}" loading="lazy">
        <p>{T('pied_txt')}</p>
      </div>
      <div>
        <h2>{T('zone_t')}</h2>
        <p>{T('zone')}</p>
      </div>
      <div>
        <h2>{T('nav')['contact']}</h2>
        <ul>
          <li><a href="tel:{SITE['tel_lien']}">{SITE['tel_affiche']}</a></li>
          <li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
          <li><a href="{SITE['instagram']}" rel="noopener">Instagram</a></li>
          <li><a href="{SITE['facebook']}" rel="noopener">Facebook</a></li>
        </ul>
      </div>
      <div>
        <h2>Navigation</h2>
        <ul>{nav}</ul>
      </div>
    </div>
    <div class="pied__bas">
      <span>© {date.today().year} {SITE['nom_long']}</span>
      <span><a href="{u('mentions')}">{T('mentions')}</a> · <a href="{u('confidentialite')}">{T('confid')}</a></span>
    </div>
  </div>
</footer>'''

ORG = {
    '@context': 'https://schema.org', '@type': 'Organization', '@id': SITE['url'] + '/#organisation',
    'name': 'Danzarina', 'alternateName': 'Association Danzarina', 'url': SITE['url'] + '/',
    'logo': SITE['url'] + '/assets/brand/logo-cercle-512.png',
    'email': SITE['email'], 'telephone': '+262 6 93 77 78 75',
    'areaServed': {'@type': 'Place', 'name': 'Saint-Joseph, La Réunion'},
    'sameAs': [SITE['instagram'], SITE['facebook']],
    'founder': {'@type': 'Person', 'name': 'Julieta'},
}

def alternates(path):
    k = cle(path)
    if not k or k in ('merci',): return ''
    out = [f'<link rel="alternate" hreflang="{lg}" href="{SITE["url"]}{u(k, lg)}">' for lg in LANGS]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{SITE["url"]}{u(k, "fr")}">')
    return '\n'.join(out)

def page(path, title, description, h1_block, body, schema=None, ogimg='/assets/brand/og-danzarina.jpg', robots='index, follow'):
    canon = SITE['url'] + path
    sch = [ORG] + (schema or [])
    ld = '\n'.join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in sch)
    doc = f'''<!doctype html>
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{T('locale')}">
{alternates(path)}
<meta property="og:site_name" content="Danzarina">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE['url']}{ogimg}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F7F3EC">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/brand/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/brand/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/fraunces-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/nunito-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/styles.css">
{ld}
</head>
<body>
{entete(path)}
<main id="contenu">
{h1_block}
{body}
</main>
{pied()}
<script src="/assets/js/menu.js" defer></script>
</body>
</html>
'''
    out = os.path.join(ROOT, path.strip('/'), 'index.html') if path != '/' else os.path.join(ROOT, 'index.html')
    if path == '/404.html': out = os.path.join(ROOT, '404.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(doc)
    return path

def titre(eyebrow, h1, lead):
    return f'''<section class="page-titre"><div class="wrap"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="lead">{lead}</p></div></section>'''

def contact_cta_s(*a, **k): return contact_cta(*a, sur_sable=True, **k)

def contact_cta(titre_txt=None, texte=None, bouton=None, sur_sable=False):
    return f'''{vague(' vague--nuit vague--sur-sable' if sur_sable else ' vague--nuit')}
<section class="section section--nuit" aria-labelledby="cta-titre"><div class="wrap">
<h2 id="cta-titre">{titre_txt or T('cta_t')}</h2><p class="lead">{texte or T('cta_x')}</p>
<div class="actions"><a class="btn btn--plein" href="{u('contact')}">{bouton or T('cta_b')}</a><a class="btn btn--contour" href="tel:{SITE['tel_lien']}">{T('appeler')} {SITE['tel_affiche']}</a></div>
</div></section>'''

def yoga_plage():
    return f'''<div class="encart">
<h3>{T('yp_t')}</h3>
<dl>
<dt>{T('yp_lieu')}</dt><dd>{T('yp_lieu_v')}</dd>
<dt>{T('yp_jour')}</dt><dd>{T('yp_jour_v')}</dd>
<dt>{T('yp_h')}</dt><dd>{T('yp_h_v')}</dd>
<dt>{T('yp_style')}</dt><dd>Shantyoga</dd>
</dl>
<p class="mention" style="margin:1rem 0 0">{T('yp_note').format(c=u('contact'))}</p>
</div>'''

pages = []

# ---------- ACCUEIL ----------
pages.append(page('/',
 'Danse & Yoga à Saint-Joseph, La Réunion | Danzarina',
 'Cours de danse et de yoga, ateliers, séances personnalisées et expériences pour hôtels à Saint-Joseph et dans le Sud de La Réunion.',
f'''<section class="hero-t" aria-labelledby="h1-accueil">
<figure class="hero-t__media">{picture('accueil-julieta-voile-terracotta', 'Julieta en équilibre sur une jambe, bras levé, tenant un voile terracotta et olive ; une grande étoffe de soie terracotta se déploie à ses côtés.', '100vw', eager=True, mobile=('accueil-julieta-voile-terracotta-4x5', '(max-width: 47.99rem)'))}<figcaption>Image artistique</figcaption></figure>
<div class="wrap hero-t__grille"><div class="hero-t__texte">
<h1 id="h1-accueil"><span class="hero-t__l1">Danse &amp; Yoga</span> <span class="hero-t__l2">La Réunion</span></h1>
<p class="lead">Cours de danse et de yoga, ateliers et séances personnalisées. Un rythme harmonieux entre danse et yoga, pour vivre son corps avec élégance et fluidité.</p>
<div class="actions"><a class="btn btn--clair" href="/yoga/">Découvrir le yoga</a><a class="btn btn--ligne" href="/danse/">Découvrir la danse</a></div>
</div></div></section>''',
 f'''<section class="manifeste" aria-label="Notre intention"><div class="wrap">
<p class="manifeste__mots"><span>Respirer</span> <span>Se recentrer</span> <span>Se relier</span></p>
<p class="manifeste__texte">Des propositions pour tous les âges et tous les niveaux, dans le respect du rythme de chacun.</p>
</div></section>

<section class="section section--sable" aria-labelledby="offre-titre"><div class="wrap">
<div class="entete-section"><p class="eyebrow">Nos axes de travail</p><h2 id="offre-titre">Bouger, respirer, se relier</h2><p class="lead">Trois axes qui unissent l’art, la santé et la communauté, pour tous les âges et tous les niveaux.</p></div>
<ol class="offres offres--lineas">
<li class="offre offre--carte"><figure class="offre__img">{picture('ambiance-yoga-tapis', 'Personne assise en méditation sur un tapis de yoga.', '(min-width: 56rem) 33vw, 100vw')}</figure><div class="offre__corps"><p class="offre__linea">Axe 1</p><h3>Santé et Bien-être</h3><p class="offre__sub">Yoga</p><p>Des cours de yoga pour prendre soin du corps, du souffle et de l’esprit. Le Shantyoga s’ajuste à chaque élève et met l’accent sur les alignements.</p><ul class="offre__items"><li>Cours de yoga</li><li>Yoga à la plage de Grand Anse</li><li>Séances personnalisées</li></ul><a class="lien-fleche" href="/yoga/">Les cours de yoga</a></div></li>
<li class="offre offre--carte"><figure class="offre__img">{picture('danse-fleurs-violettes', 'Un couple danse en plein air au milieu des lavandes.', '(min-width: 56rem) 33vw, 100vw')}</figure><div class="offre__corps"><p class="offre__linea">Axe 2</p><h3>Communauté et Bien-être</h3><p class="offre__sub">Danse</p><p>Danser ensemble pour créer des liens, gagner en confiance et profiter du mouvement et de la rencontre.</p><ul class="offre__items"><li>Tango et folklore argentin</li><li>Salsa et rythmes latins</li><li>Femmes en mouvement</li></ul><p class="offre__nota"><strong>Femmes en mouvement:</strong> un espace de danse pour les femmes de tout âge, avec ou sans expérience, pour bouger, créer et vivre de nouvelles expériences dans une ambiance chaleureuse et bienveillante.</p><a class="lien-fleche" href="/danse/">Les cours de danse</a></div></li>
<li class="offre offre--carte"><figure class="offre__img">{picture('mouvement-sous-le-ciel-4x5', 'Un couple danse en plein air, avec des montagnes et un ciel nuageux en arrière-plan.', '(min-width: 56rem) 33vw, 100vw')}</figure><div class="offre__corps"><p class="offre__linea">Axe 3</p><h3>Expériences créatives</h3><p class="offre__sub">Rencontres ponctuelles</p><p>Ateliers, rencontres conviviales et expériences qui unissent danse et yoga dans la nature, à l’hôtel et dans des lieux culturels. Chaque rencontre, une expérience inoubliable.</p><ul class="offre__items"><li>Ateliers de danse et de yoga</li><li>Rencontres conviviales</li><li>Expériences pour hôtels</li></ul><div class="offre__agenda"><p class="offre__agenda-t"><strong>Rencontres en plein air</strong><br>Tous les mardis, de 9h30 à 10h45 · lieu à confirmer</p></div><a class="lien-fleche" href="/ateliers/">Voir les ateliers</a></div></li>
</ol>
</div></section>

<section class="section section--olive" aria-labelledby="plage-titre"><div class="wrap duo">
<div>
<p class="eyebrow">Rendez-vous de la semaine</p>
<h2 id="plage-titre">Yoga à la plage, le mardi matin</h2>
<p class="lead">Le Shantyoga s’ajuste à chaque élève et met beaucoup l’accent sur les alignements : écoute du corps, respiration, alignement, présence et bien-être.</p>
<a class="lien-fleche" href="/yoga/">Tout savoir sur le yoga</a>
</div>
{yoga_plage()}
</div></section>

<figure class="bandeau bandeau--x">
{picture('danse-canape-ciel-2x1', 'Un danseur soutient une danseuse en extension au-dessus d’un canapé ancien posé dans un pré, devant une botte de foin et des montagnes au coucher du soleil.', '100vw', mobile=('danse-canape-ciel-4x5', '(max-width: 35.99rem)'))}
<figcaption class="bandeau__phrase">« Le corps ouvre un espace »</figcaption>
</figure>

<section class="section" aria-labelledby="parcours-titre"><div class="wrap duo duo--inverse">
<figure class="cadre-decale">{picture('parcours-noir-et-blanc', 'Photo en noir et blanc : une danseuse debout sur un canapé ancien installé dans un champ, un homme assis à côté d’elle, des montagnes au loin.', '(min-width: 56rem) 50vw, 100vw')}<figcaption>Archives Danzarina.</figcaption></figure>
<div>
<p class="eyebrow">Un parcours en mouvement</p>
<h2 id="parcours-titre">Une vie à danser, à transmettre</h2>
<p>Danzarina est née de la volonté de créer un espace dédié à l’exploration du mouvement et de la spiritualité à travers la danse et le yoga.</p>
<p>Derrière Danzarina, il y a Julieta, artiste du mouvement d’origine argentine, avec plus de 20 ans de formation en ballet, jazz, danse contemporaine, tango, folklore argentin, salsa, zouk et kizomba. Aujourd’hui, elle allie la danse et le yoga dans sa propre méthode d’enseignement.</p>
<p>Aujourd’hui, Danzarina poursuit son chemin à La Réunion.</p>
<a class="lien-fleche" href="/a-propos/">Découvrir notre histoire</a>
</div>
</div></section>

<section class="section section--sable" aria-label="Pour aller plus loin"><div class="wrap tuiles">
<article class="tuile tuile--terre"><p class="eyebrow">Professionnels</p><h2 class="tuile__titre">Hôtels &amp; partenaires</h2><p>Des séances de danse ou de yoga au sein de votre établissement, adaptées à votre lieu et à vos hôtes.</p><a class="btn btn--clair" href="/hotels-partenaires/">Parler de votre projet</a></article>
<article class="tuile tuile--olive"><p class="eyebrow">Rendez-vous ponctuels</p><h2 class="tuile__titre">Ateliers</h2><p>Des ateliers pour approfondir une pratique. Les prochaines dates seront annoncées ici et sur Instagram.</p><a class="btn btn--clair" href="/ateliers/">Voir les ateliers</a></article>
</div></section>
{contact_cta_s()}''',
 schema=[{'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Danzarina', 'url': SITE['url'] + '/', 'inLanguage': 'fr-FR'}]))

# ---------- DANSE ----------
pages.append(page('/danse/',
 'Cours de danse à Saint-Joseph, La Réunion : tango, salsa, enfants | Danzarina',
 'Cours de danse avec Danzarina dans le Sud de La Réunion : tango et salsa pour adultes, danse pour enfants. Une pratique à votre rythme, sans pression.',
 titre('Danse', 'Cours de danse', 'Danser pour le plaisir du mouvement, de la musique et de la rencontre, à votre rythme et sans esprit de compétition.'),
 f'''<section class="section" style="padding-top:0"><div class="wrap">
{picture('hero-danse-a-deux-16x9', 'Un couple danse à deux dans une prairie, en t-shirts orange, au soleil de fin de journée.', '(min-width: 72rem) 68rem, 100vw', cls='', mobile=('hero-danse-a-deux-4x5', '(max-width: 35.99rem)'))}
</div></section>
<section class="section" style="padding-top:0" aria-labelledby="styles-titre"><div class="wrap">
<h2 id="styles-titre">Les danses proposées</h2>
<div class="grille grille--3">
<article class="carte"><h3>Tango</h3><p>Pour adultes. Une danse d’écoute et de connexion, où l’on apprend à marcher ensemble.</p></article>
<article class="carte"><h3>Salsa</h3><p>Pour adultes. Une danse joyeuse et rythmée, pour se lâcher et partager.</p></article>
<article class="carte"><h3>Danse pour enfants</h3><p>Éveil et découverte du mouvement, de la musique et de l’expression.</p></article>
</div>
</div></section>
{vague()}
<section class="section section--sable" aria-labelledby="methode-titre"><div class="wrap duo">
<div>
<h2 id="methode-titre">Notre façon de transmettre</h2>
<ul class="liste-points">
<li>Ouvert à toutes et à tous, débutants comme pratiquants.</li>
<li>On avance à son rythme : pas de performance à atteindre.</li>
<li>Seul ou à deux : pas besoin de venir avec un partenaire.</li>
<li>Une attention portée à l’écoute du corps et à la connexion.</li>
</ul>
<h3 id="horaires">Horaires, lieux et tarifs</h3>
<p>Les horaires et lieux des cours de danse de la nouvelle saison seront publiés ici prochainement. En attendant, <a href="/contact/">contactez-nous</a> pour être informé·e.</p>
</div>
<figure>{picture('danse-fleurs-violettes', 'Deux danseurs se font face en pleine figure de danse à deux, au milieu de fleurs violettes, sous un ciel bleu.', '(min-width: 56rem) 50vw, 100vw')}</figure>
</div></section>
{vague(' vague--haut')}
<section class="section" aria-labelledby="galerie-titre"><div class="wrap">
<h2 id="galerie-titre">En mouvement</h2>
<ul class="galerie">
<li>{picture('danse-canape-paysage', 'Un danseur soutient une danseuse en extension au-dessus d’un canapé ancien posé dans l’herbe, montagnes en arrière-plan.', '(min-width: 60rem) 33vw, 100vw')}</li>
<li>{picture('mouvement-sous-le-ciel-4x5', 'Deux danseurs en plein élan dans un champ, sous un ciel nuageux.', '(min-width: 60rem) 33vw, 100vw')}</li>
<li>{picture('parcours-noir-et-blanc', 'Photo en noir et blanc de deux danseurs autour d’un canapé ancien dans un champ.', '(min-width: 60rem) 33vw, 100vw')}</li>
</ul>
</div></section>
{contact_cta('Envie de danser ?', 'Dites-nous ce qui vous attire, nous vous orientons vers la proposition qui vous correspond.')}''',
 schema=[{'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
   {'@type': 'ListItem', 'position': 1, 'name': 'Accueil', 'item': SITE['url'] + '/'},
   {'@type': 'ListItem', 'position': 2, 'name': 'Danse', 'item': SITE['url'] + '/danse/'}]}]))

# ---------- YOGA ----------
pages.append(page('/yoga/',
 'Cours de yoga à Saint-Joseph : Shantyoga à la plage de Grand Anse | Danzarina',
 'Cours de Shantyoga à Saint-Joseph, La Réunion : yoga à la plage de Grand Anse le mardi de 9h30 à 11h. Un yoga qui s’ajuste à chaque élève.',
 titre('Yoga', 'Cours de yoga à Saint-Joseph', 'Le Shantyoga : un style de yoga qui s’ajuste à chaque élève et qui met beaucoup l’accent sur les alignements.'),
 f'''<section class="section" style="padding-top:0"><div class="wrap duo">
<div>
<h2>Notre approche</h2>
<p>Chaque séance laisse le temps d’arriver, de respirer et d’écouter son corps. Les postures sont adaptées à chacun : l’important n’est pas d’aller loin, mais d’être juste.</p>
<ul class="liste-points">
<li>Écoute du corps</li><li>Respiration</li><li>Alignement</li><li>Présence</li><li>Bien-être</li>
</ul>
</div>
{yoga_plage()}
</div></section>
<figure class="bandeau bandeau--doux">{picture('ambiance-yoga-tapis', '', '100vw')}</figure>
{vague()}
<section class="section section--sable" aria-labelledby="pratique-titre"><div class="wrap">
<h2 id="pratique-titre">Infos pratiques</h2>
<div class="grille grille--3">
<article class="carte"><h3>Niveau</h3><p>Ouvert à toutes et à tous, quel que soit votre âge ou votre niveau.</p></article>
<article class="carte"><h3>Matériel</h3><p>Une tenue confortable. Pour le tapis et le reste, <a href="/contact/">demandez-nous</a> avant votre première séance.</p></article>
<article class="carte"><h3>Santé</h3><p>Le yoga ne remplace pas un avis médical. En cas de grossesse, de blessure ou de problème de santé, parlez-en à votre médecin et prévenez-nous avant la séance.</p></article>
</div>
</div></section>
{vague(' vague--haut')}
<section class="section" aria-labelledby="enseignante-titre"><div class="wrap">
<h2 id="enseignante-titre">L’enseignante</h2>
<p>Julieta est certifiée Shantyoga 200 heures (2019, formation reconnue par Yoga Alliance) et se forme au yoga Iyengar.</p>
<a class="lien-fleche" href="/a-propos/">En savoir plus sur Julieta</a>
</div></section>
{contact_cta('Envie d’essayer ?', 'Écrivez-nous pour connaître les prochaines séances et réserver votre place.')}''',
 schema=[{'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
   {'@type': 'ListItem', 'position': 1, 'name': 'Accueil', 'item': SITE['url'] + '/'},
   {'@type': 'ListItem', 'position': 2, 'name': 'Yoga', 'item': SITE['url'] + '/yoga/'}]}]))

# ---------- COURS PERSONNALISÉS ----------
pages.append(page('/cours-personnalises/',
 'Cours particuliers de danse et de yoga à Saint-Joseph | Danzarina',
 'Séances personnalisées de danse ou de yoga dans le Sud de La Réunion : un échange, un objectif, un format adapté et un suivi.',
 titre('Cours personnalisés', 'Cours personnalisés de danse et de yoga', 'Une séance pensée pour vous : seul·e, en couple ou en petit groupe, autour d’un objectif qui vous ressemble.'),
 f'''<section class="section" style="padding-top:0" aria-labelledby="etapes-titre"><div class="wrap">
<h2 id="etapes-titre">Comment ça se passe</h2>
<ol class="etapes">
<li><h3>Un premier échange</h3><p>Vous nous parlez de vous, de vos envies et de vos éventuelles contraintes.</p></li>
<li><h3>Votre objectif</h3><p>Ouvrir le bal d’un mariage, reprendre le mouvement, approfondir une pratique…</p></li>
<li><h3>Une proposition</h3><p>Nous vous proposons un format : durée, nombre de séances, danse ou yoga.</p></li>
<li><h3>La séance</h3><p>Un moment à votre rythme, centré sur vous.</p></li>
<li><h3>Le suivi</h3><p>Nous faisons le point ensemble et ajustons la suite.</p></li>
</ol>
</div></section>
{vague()}
<section class="section section--sable"><div class="wrap">
<h2>Lieu et modalités</h2>
<p>Les lieux possibles, les tarifs et les modalités de déplacement vous sont précisés lors du premier échange.</p>
</div></section>
{contact_cta_s('Parlons de votre projet', 'Décrivez-nous votre envie en quelques lignes : nous revenons vers vous pour en discuter.', 'Demander une séance')}'''))

# ---------- ATELIERS ----------
pages.append(page('/ateliers/',
 'Ateliers de danse et de yoga à Saint-Joseph, La Réunion | Danzarina',
 'Les ateliers Danzarina de danse et de yoga dans le Sud de La Réunion : dates, lieux et réservations.',
 titre('Ateliers', 'Ateliers de danse et de yoga', 'Des rendez-vous ponctuels pour approfondir une pratique, découvrir une danse ou prendre un temps pour soi.'),
 f'''<section class="section" style="padding-top:0"><div class="wrap">
<div class="encart">
<h2 style="font-size:1.4rem">Prochains ateliers</h2>
<p>Aucun atelier n’est programmé pour le moment. Les prochaines dates seront annoncées sur cette page et sur <a href="{SITE['instagram']}" rel="noopener">Instagram</a>.</p>
<p style="margin:0">Vous souhaitez être prévenu·e ? <a href="/contact/">Écrivez-nous</a>.</p>
</div>
</div></section>
{contact_cta()}'''))

# ---------- HÔTELS ----------
pages.append(page('/hotels-partenaires/',
 'Danse et yoga pour hôtels et hébergements à La Réunion | Danzarina',
 'Séances de yoga et de danse pour hôtels, gîtes et hébergements du Sud de La Réunion : formats adaptables, intervention sur place, devis selon votre projet.',
 titre('Hôtels & partenaires', 'Danse et yoga pour hôtels et hébergements', 'Une proposition de bien-être et de mouvement pour vos hôtes, construite avec vous selon votre établissement.'),
 f'''<section class="section" style="padding-top:0" aria-labelledby="formats-titre"><div class="wrap">
<h2 id="formats-titre">Ce que nous pouvons construire ensemble</h2>
<div class="grille grille--2">
<article class="carte"><h3>Des formats adaptables</h3><p>Yoga, danse ou initiation, en séance ponctuelle ou régulière, selon le rythme de votre établissement.</p></article>
<article class="carte"><h3>Une intervention chez vous</h3><p>Nous nous déplaçons dans votre établissement, en intérieur ou en extérieur selon les espaces disponibles.</p></article>
<article class="carte"><h3>Selon votre public</h3><p>Une proposition pensée selon le nombre de participants, leurs attentes et le contexte de votre lieu.</p></article>
<article class="carte"><h3>Un devis clair</h3><p>Après un premier échange, nous vous adressons une proposition détaillée.</p></article>
</div>
</div></section>
<figure class="bandeau bandeau--doux">{picture('ambiance-frangipanier', '', '100vw')}</figure>
{vague()}
<section class="section section--sable" aria-labelledby="infos-titre"><div class="wrap">
<h2 id="infos-titre">Pour préparer votre demande</h2>
<ul class="liste-points">
<li>Le nom et la localisation de votre établissement</li>
<li>Le type de séance qui vous intéresse (yoga, danse, les deux)</li>
<li>Le nombre de participants envisagé</li>
<li>Les espaces disponibles et les périodes souhaitées</li>
</ul>
</div></section>
{contact_cta_s('Parler de votre projet', 'Présentez-nous votre établissement et vos envies, nous revenons vers vous rapidement.', 'Parler de votre projet')}'''))

# ---------- À PROPOS ----------
pages.append(page('/a-propos/',
 'À propos de Danzarina : Julieta, danse et yoga à La Réunion | Danzarina',
 'L’histoire de Danzarina et de Julieta, artiste du mouvement d’origine argentine : danse, Shantyoga et une nouvelle étape à La Réunion.',
 titre('À propos', 'À propos de Danzarina', 'Danzarina est née de la volonté de créer un espace dédié à l’exploration du mouvement et de la spiritualité à travers la danse et le yoga.'),
 f'''<section class="section" style="padding-top:0" aria-labelledby="julieta-titre"><div class="wrap duo">
<figure>{picture('portrait-editorial-julieta', 'Portrait artistique de Julieta marchant pieds nus sur un sentier, en jupe longue et voiles superposés, au coucher du soleil.', '(min-width: 56rem) 50vw, 100vw')}<figcaption>Portrait artistique.</figcaption></figure>
<div>
<p class="eyebrow">La fondatrice</p>
<h2 id="julieta-titre">Julieta</h2>
<h3>Son histoire</h3>
<p>Artiste du mouvement d’origine argentine, Julieta se forme à la danse depuis plus de 20 ans. Danseuse de ballet, jazz, danse contemporaine, tango, folklore argentin, salsa, zouk et kizomba, elle s’est spécialisée dans chacun de ces styles.</p>
<p>Elle a mené un long parcours dans la danse et à travers le monde, en transmettant son savoir dans différentes villes et écoles de danse en Russie, en Espagne et en France.</p>
<h3>Sa formation</h3>
<ul class="liste-points">
<li>Plus de 20 ans de formation en danse : ballet, jazz, danse contemporaine, tango, folklore argentin, salsa, zouk et kizomba, entre autres</li>
<li>Formation auprès d’artistes et de maîtres renommés en Russie, en Argentine (Córdoba, Buenos Aires), en Espagne et en France</li>
<li>Certification Shantyoga 200 heures (2019), formation reconnue par Yoga Alliance</li>
<li>Actuellement en formation au yoga Iyengar</li>
</ul>
<h3>Son chemin dans le yoga</h3>
<p>Aujourd’hui, elle poursuit son chemin dans le yoga et crée son propre système d’enseignement, dans lequel elle met en pratique tout ce qu’elle a appris au cours d’une vie consacrée au mouvement. Elle enseigne la danse aux enfants, le tango et la salsa aux adultes, ainsi que le yoga.</p>
</div>
</div></section>
{vague()}
<section class="section section--sable" aria-labelledby="parcours-titre"><div class="wrap duo duo--inverse">
<figure>{picture('danse-canape-paysage', 'Un danseur soutient une danseuse en extension au-dessus d’un canapé ancien posé dans l’herbe, montagnes en arrière-plan.', '(min-width: 56rem) 50vw, 100vw')}<figcaption>Archives Danzarina.</figcaption></figure>
<div>
<p class="eyebrow">Un parcours en mouvement</p>
<h2 id="parcours-titre">Danser à deux</h2>
<p>Julieta partage la danse avec Christian, pédago-danseur, avec qui elle danse le tango et la salsa. Christian a appris la danse africaine auprès de Hamed.</p>
</div>
</div></section>
{vague(' vague--haut')}
<section class="section" aria-labelledby="vision-titre"><div class="wrap">
<p class="eyebrow">La vision de Danzarina</p>
<h2 id="vision-titre">Une terre, le même mouvement</h2>
<p>Simplicité, nature, paix et fraternité : Danzarina veut offrir un espace où chacun peut bouger, respirer et se relier, quel que soit son âge ou son niveau. Après un chemin en mouvement, Danzarina poursuit aujourd’hui son activité à Saint-Joseph, dans le Sud de La Réunion.</p>
</div></section>
{contact_cta()}''',
 schema=[{'@context': 'https://schema.org', '@type': 'Person', 'name': 'Julieta', 'jobTitle': 'Professeure de danse et de yoga', 'worksFor': {'@id': SITE['url'] + '/#organisation'}}]))

# ---------- CONTACT ----------
pages.append(page('/contact/',
 'Contact | Danzarina, danse et yoga à Saint-Joseph',
 'Contactez Danzarina pour les cours de danse et de yoga à Saint-Joseph et dans le Sud de La Réunion : téléphone, e-mail, formulaire.',
 titre('Contact', 'Contact', f'Une question sur les cours, un projet pour votre établissement ? Nous intervenons à {SITE["zone"]}.'),
 f'''<section class="section" style="padding-top:0"><div class="wrap duo" style="align-items:start">
<div>
<h2>Nous joindre</h2>
<ul class="coord">
<li>Téléphone : <a href="tel:{SITE['tel_lien']}">&nbsp;{SITE['tel_affiche']}</a></li>
<li>E-mail : <a href="mailto:{SITE['email']}">&nbsp;{SITE['email']}</a></li>
<li>Instagram : <a href="{SITE['instagram']}" rel="noopener">&nbsp;{SITE['instagram_nom']}</a></li>
<li>Facebook : <a href="{SITE['facebook']}" rel="noopener">&nbsp;Danzarina France</a></li>
</ul>
<h2 style="margin-top:2.5rem">Questions fréquentes</h2>
<div class="faq">
<details><summary>Faut-il avoir déjà pratiqué ?</summary><p>Non. Les cours sont ouverts à toutes et à tous, quel que soit le niveau.</p></details>
<details><summary>Faut-il venir avec un partenaire pour danser ?</summary><p>Non, vous pouvez venir seul·e.</p></details>
<details><summary>Où ont lieu les cours de yoga ?</summary><p>Le yoga à la plage a lieu à Grand Anse, à Saint-Joseph, le mardi de 9h30 à 11h.</p></details>
</div>
</div>
<div>
<h2>Écrire un message</h2>
<form class="form" name="contact" method="POST" action="/merci/" data-netlify="true" netlify-honeypot="site-web" data-valider data-email="{T('email_inv')}" data-requis="{T('requis')}">
<input type="hidden" name="form-name" value="contact">
<input type="hidden" name="langue" value="fr">
<p class="cache"><label>Ne pas remplir : <input name="site-web" tabindex="-1" autocomplete="off"></label></p>
<p class="mention" style="margin:0">Les champs marqués d’un astérisque (*) sont obligatoires.</p>
<div class="champ"><label for="nom">Nom et prénom *</label><input id="nom" name="nom" type="text" autocomplete="name" required aria-describedby="nom-erreur" data-vide="Indiquez votre nom."><span class="erreur" id="nom-erreur" aria-live="polite"></span></div>
<div class="champ"><label for="email">E-mail *</label><input id="email" name="email" type="email" autocomplete="email" required aria-describedby="email-erreur" data-vide="Indiquez votre adresse e-mail."><span class="erreur" id="email-erreur" aria-live="polite"></span></div>
<div class="champ"><label for="tel">Téléphone</label><span class="aide" id="tel-aide">Facultatif, si vous préférez être rappelé·e.</span><input id="tel" name="telephone" type="tel" autocomplete="tel" aria-describedby="tel-aide"></div>
<div class="champ"><label for="sujet">Votre demande concerne</label><select id="sujet" name="sujet"><option>Danse</option><option>Yoga</option><option>Cours personnalisés</option><option>Ateliers</option><option>Hôtels &amp; partenaires</option><option>Autre</option></select></div>
<div class="champ"><label for="message">Message *</label><textarea id="message" name="message" required aria-describedby="message-erreur" data-vide="Écrivez votre message."></textarea><span class="erreur" id="message-erreur" aria-live="polite"></span></div>
<p class="mention">Vos données servent uniquement à répondre à votre demande. Voir notre <a href="/politique-de-confidentialite/">politique de confidentialité</a>.</p>
<button class="btn btn--plein" type="submit">Envoyer le message</button>
</form>
</div>
</div></section>''',
 schema=[{'@context': 'https://schema.org', '@type': 'ContactPage', 'name': 'Contact Danzarina', 'url': SITE['url'] + '/contact/'}]))

# ---------- MERCI ----------
pages.append(page('/merci/', 'Message envoyé | Danzarina', 'Votre message a bien été envoyé à Danzarina.',
 titre('Merci', 'Message envoyé', 'Merci pour votre message. Nous vous répondons dès que possible.'),
 '<section class="section" style="padding-top:0"><div class="wrap"><a class="btn btn--plein" href="/">Retour à l’accueil</a></div></section>', robots='noindex, follow'))

# ---------- LÉGAL ----------
AC = '<span class="a-completer">[À COMPLÉTER]</span>'
pages.append(page('/mentions-legales/', 'Mentions légales | Danzarina', 'Mentions légales du site danzarina.fr.',
 titre('Informations légales', 'Mentions légales', 'Conformément à la loi n° 2004-575 du 21 juin 2004 pour la confiance dans l’économie numérique (LCEN).'),
 f'''<section class="section contenu-legal" style="padding-top:0"><div class="wrap">
<h2>Éditeur du site</h2>
<p>{SITE['nom_long']}, association {AC}<br>Siège social : {AC}<br>Numéro RNA : {AC} · SIRET (le cas échéant) : {AC}<br>Téléphone : {SITE['tel_affiche']} · E-mail : <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
<h2>Directeur·rice de la publication</h2>
<p>{AC}</p>
<h2>Hébergement</h2>
<p>Netlify, Inc., 512 2nd Street, Suite 200, San Francisco, CA 94107, États-Unis · <a href="https://www.netlify.com" rel="noopener">www.netlify.com</a></p>
<h2>Propriété intellectuelle</h2>
<p>L’ensemble des contenus de ce site (textes, photographies, logo) est la propriété de Danzarina ou de leurs auteurs. Toute reproduction sans autorisation est interdite. Les personnes photographiées ont donné leur accord pour la diffusion de leur image.</p>
<h2>Crédits</h2>
<p>Photographies : {AC}. Le portrait de la page À propos est une image artistique.</p>
</div></section>''', robots='noindex, follow'))

pages.append(page('/politique-de-confidentialite/', 'Politique de confidentialité | Danzarina', 'Politique de confidentialité et de protection des données personnelles du site danzarina.fr.',
 titre('Données personnelles', 'Politique de confidentialité', 'Comment nous traitons les données que vous nous confiez, conformément au RGPD et à la loi Informatique et Libertés.'),
 f'''<section class="section contenu-legal" style="padding-top:0"><div class="wrap">
<h2>Responsable du traitement</h2>
<p>{SITE['nom_long']}, {AC} · <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
<h2>Données collectées</h2>
<p>Via le formulaire de contact : nom, adresse e-mail, téléphone (facultatif), objet et contenu de votre message. Aucune autre donnée n’est collectée.</p>
<h2>Finalité et base légale</h2>
<p>Répondre à votre demande (intérêt légitime, ou mesures précontractuelles si vous demandez un devis).</p>
<h2>Destinataires</h2>
<p>Seule l’équipe de Danzarina. Les messages transitent par notre hébergeur, Netlify (service Netlify Forms), situé aux États-Unis et encadré par les clauses contractuelles types de la Commission européenne.</p>
<h2>Durée de conservation</h2>
<p>Trois ans à compter de notre dernier échange, puis suppression.</p>
<h2>Cookies et mesure d’audience</h2>
<p>Ce site n’utilise aucun cookie de mesure d’audience ni de publicité, et ne fait appel à aucun service tiers de suivi. Les polices de caractères sont hébergées sur notre propre serveur.</p>
<h2>Vos droits</h2>
<p>Vous disposez d’un droit d’accès, de rectification, d’effacement, de limitation, d’opposition et de portabilité. Pour les exercer : <a href="mailto:{SITE['email']}">{SITE['email']}</a>. Vous pouvez aussi introduire une réclamation auprès de la CNIL (<a href="https://www.cnil.fr" rel="noopener">www.cnil.fr</a>).</p>
<p class="mention">Dernière mise à jour : {AC}</p>
</div></section>''', robots='noindex, follow'))

pages.append(page('/404.html', 'Page introuvable | Danzarina', 'Cette page n’existe pas ou a été déplacée.',
 titre('Erreur 404', 'Page introuvable', 'Cette page n’existe pas ou a été déplacée.'),
 '<section class="section" style="padding-top:0"><div class="wrap"><div class="actions"><a class="btn btn--plein" href="/">Retour à l’accueil</a><a class="btn btn--contour" href="/contact/">Nous contacter</a></div></div></section>', robots='noindex, follow'))

# ---------- Espagnol et anglais ----------
for _lg in ('es', 'en'):
    L = _lg
    exec(open(os.path.join(ROOT, 'tools', f'pages_{_lg}.py'), encoding='utf-8').read())
L = 'fr'

# ---------- sitemap (avec versions linguistiques) ----------
cles = ['accueil', 'danse', 'yoga', 'perso', 'ateliers', 'hotels', 'apropos', 'contact']
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for k in cles:
    alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{lg}" href="{SITE["url"]}{u(k, lg)}"/>' for lg in LANGS) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE["url"]}{u(k, "fr")}"/>'
    for lg in LANGS:
        sm.append(f'  <url><loc>{SITE["url"]}{u(k, lg)}</loc><lastmod>{TODAY}</lastmod>{alts}</url>')
sm.append('</urlset>')
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('\n'.join(sm) + '\n')
print('pages:', len(pages))
