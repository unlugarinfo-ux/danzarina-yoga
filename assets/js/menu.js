// Menu mobile accessible (seul JavaScript du site, avec la validation du formulaire)
(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  if (btn && nav) {
    function fermer() { btn.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); }
    btn.addEventListener('click', function () {
      var ouvert = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!ouvert));
      nav.classList.toggle('is-open', !ouvert);
      if (!ouvert) { var l = nav.querySelector('a'); if (l) l.focus(); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') { fermer(); btn.focus(); }
    });
  }

  // Validation du formulaire de contact avec messages compréhensibles
  var form = document.querySelector('form[data-valider]');
  if (!form) return;
  form.setAttribute('novalidate', '');
  form.addEventListener('submit', function (e) {
    var premier = null;
    form.querySelectorAll('[required]').forEach(function (champ) {
      var msg = document.getElementById(champ.id + '-erreur');
      var texte = '';
      if (!champ.value.trim()) texte = champ.dataset.vide || form.dataset.requis || 'Ce champ est obligatoire.';
      else if (champ.type === 'email' && !champ.validity.valid) texte = form.dataset.email || 'Indiquez une adresse e-mail valide, par exemple nom@exemple.fr.';
      champ.setAttribute('aria-invalid', texte ? 'true' : 'false');
      if (msg) msg.textContent = texte;
      if (texte && !premier) premier = champ;
    });
    if (premier) { e.preventDefault(); premier.focus(); }
  });
})();
