window.JPWP = {
  openTOC: function(){
    document.body.classList.add('wp-toc-open');
  },
  closeTOC: function(){
    document.body.classList.remove('wp-toc-open');
  }
};
// Close TOC when clicking a link on mobile
document.addEventListener('click', function(e){
  var a = e.target.closest && e.target.closest('.wp-toc a');
  if(a && document.body.classList.contains('wp-toc-open')){
    document.body.classList.remove('wp-toc-open');
  }
});
