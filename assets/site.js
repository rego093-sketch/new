(function(){
  const btn = document.getElementById('tocToggle');
  const sidebar = document.getElementById('sidebar');
  if(btn && sidebar){
    btn.addEventListener('click', function(){
      sidebar.classList.toggle('open');
      const expanded = sidebar.classList.contains('open');
      btn.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    });
    sidebar.addEventListener('click', function(e){
      const a = e.target.closest('a');
      if(a && sidebar.classList.contains('open')){
        sidebar.classList.remove('open');
        btn.setAttribute('aria-expanded','false');
      }
    });
  }
})();