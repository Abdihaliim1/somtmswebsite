(function(){
  const path = location.pathname.replace(/\/+$|^\/$/g, '') || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(a=>{
    const href = (a.getAttribute('href')||'').replace(/\/+$|^\/$/g, '') || 'index.html';
    if(href === path) a.classList.add('active');
  });

  // Mobile Menu
  const toggle = document.querySelector('.mobile-toggle');
  const menu = document.querySelector('.mobile-menu');
  if(toggle && menu){
    toggle.addEventListener('click', ()=>{
      menu.classList.toggle('active');
      const spans = toggle.querySelectorAll('span');
      // simple toggle animation
      if(menu.classList.contains('active')){
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
      } else {
        spans[0].style.transform = 'none';
        spans[1].style.opacity = '1';
        spans[2].style.transform = 'none';
      }
    });
  }
})();
