# danzarina.fr

Site statique de Danzarina (danse & yoga, Saint-Joseph, La Réunion). Aucun build côté Netlify : `publish = "."`.

- Modifier les textes : `tools/build.py`, puis `python3 tools/build.py` (régénère les pages et `sitemap.xml`).
- Images : originaux dans `assets/images/originals/`, dérivés AVIF/WebP/JPEG dans `assets/images/optimized/` via `python3 tools/images.py`.
- Formulaire : Netlify Forms (`contact`).
- Redirections des anciennes URLs : `netlify.toml`.
