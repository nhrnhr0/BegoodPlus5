console.log('home.js');
//$('body').css('display','none');
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 'auto',
    //spaceBetween: 30,
    freeMode: true,
    speed: 4000,
    spaceBetween: 100,
    loop:true,
    //effect: 'flip',
    centeredSlides: true,
    loopedSlides:6,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    autoplay: {
      disableOnInteraction:false,
      delay:0,
    },
  });