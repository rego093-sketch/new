(function(){
  function getLang(){
    if (location.pathname.startsWith('/ko/')) return 'ko';
    return 'en';
  }
  function slugify(s){
    return (s||'').toLowerCase()
      .replace(/[^a-z0-9\uac00-\ud7a3\s\-]/g,'')
      .trim().replace(/\s+/g,'-')
      .slice(0,80) || ('sec-' + Math.random().toString(36).slice(2,8));
  }
  function buildSelect(){
    var sel = document.getElementById('paperSelect');
    if(!sel || !window.JP_PAPERS) return;
    var lang = getLang();
    var papers = window.JP_PAPERS.papers || [];
    sel.innerHTML = '';
    var ph = document.createElement('option');
    ph.value = '';
    ph.textContent = (lang==='ko') ? '백서 선택' : 'Select whitepaper';
    sel.appendChild(ph);
    papers.forEach(function(p){
      var o = document.createElement('option');
      o.value = (lang==='ko') ? p.path_ko : p.path_en;
      o.textContent = (lang==='ko') ? p.title_ko : p.title_en;
      sel.appendChild(o);
    });
    sel.addEventListener('change', function(){
      if(!sel.value) return;
      location.href = sel.value;
    });
  }
  function buildTOC(){
    var tocHost = document.getElementById('autoTOC');
    if(!tocHost) return;
    var content = document.querySelector('.wp-content') || document;
    var heads = content.querySelectorAll('h2, h3, h4');
    if(!heads.length){
      tocHost.textContent = '—';
      return;
    }
    // Ensure ids
    heads.forEach(function(h){
      if(!h.id){
        h.id = slugify(h.textContent);
      }
    });
    // Build nested list
    var root = document.createElement('ul');
    var stack = [{level:2, ul:root}];
    function levelOf(tag){ return parseInt(tag.replace('H',''),10); }
    heads.forEach(function(h){
      var lvl = levelOf(h.tagName);
      // normalize to 2-4
      if(lvl < 2) lvl = 2;
      if(lvl > 4) lvl = 4;
      while(stack.length && lvl < stack[stack.length-1].level){
        stack.pop();
      }
      while(stack.length && lvl > stack[stack.length-1].level){
        // create nested ul under last li
        var lastUl = stack[stack.length-1].ul;
        var lastLi = lastUl.lastElementChild;
        if(!lastLi){
          // create a dummy
          lastLi = document.createElement('li');
          lastUl.appendChild(lastLi);
        }
        var nu = document.createElement('ul');
        lastLi.appendChild(nu);
        stack.push({level: stack[stack.length-1].level+1, ul: nu});
      }
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent;
      li.appendChild(a);
      stack[stack.length-1].ul.appendChild(li);
    });
    tocHost.innerHTML = '';
    tocHost.appendChild(root);
  }
  document.addEventListener('DOMContentLoaded', function(){
    buildSelect();
    buildTOC();
  });
})();
