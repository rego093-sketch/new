(function () {
  function normalizeLang(path) {
    if (path.startsWith('/ko/')) return 'ko';
    return 'en';
  }
  function currentLang() { return normalizeLang(location.pathname); }

  function buildSelect() {
    var sel = document.getElementById('paperSelect');
    if (!sel || !window.JP_PAPERS) return;

    var lang = currentLang();
    var papers = window.JP_PAPERS;

    // Build options (prefer current language path; fallback to english)
    sel.innerHTML = '';
    papers.forEach(function(p) {
      var opt = document.createElement('option');
      opt.value = (p.paths && p.paths[lang]) ? p.paths[lang] : (p.paths && p.paths.en) ? p.paths.en : (p.doi ? ('https://doi.org/' + p.doi) : '/');
      opt.textContent = p.short + ' — ' + p.title[lang];
      sel.appendChild(opt);
    });

    // Select current page if matches
    var here = location.pathname.replace(/index\.html$/, '');
    for (var i = 0; i < sel.options.length; i++) {
      var v = sel.options[i].value;
      if (v === here || v === location.pathname) { sel.selectedIndex = i; break; }
    }

    sel.addEventListener('change', function() {
      var dest = sel.value;
      if (dest) location.href = dest;
    });
  }

  document.addEventListener('DOMContentLoaded', buildSelect);
})();
