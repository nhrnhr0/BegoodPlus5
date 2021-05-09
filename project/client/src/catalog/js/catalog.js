console.log('hey catalog.js');

var swipers = [];
        var swiperDom = document.querySelectorAll('.swiper-category');//$('.swiper-category');
        for (var i = 0; i < swiperDom.length; i++) {
            swipers.push(new Swiper(swiperDom[i], {
                // Enable lazy loading
                //lazy: true,
                effect: 'coverflow',
                grabCursor: true,
                speed: 125,
                loop: true,
                centeredSlides: true,
                slidesPerView: 5,
                loopedSlides: 10,
                //checkInView: true,
                slideToClickedSlide: true,
                // Disable preloading of all images
                preloadImages: true,
                // Enable lazy loading
                lazy: {
                    loadOnTransitionStart: true,
                    checkInView:true,
                    loadPrevNext:true,
                    loadPrevNextAmount:8,
                },
                watchSlidesVisibility: true,
                coverflowEffect: {
                    rotate: -13,
                    stretch: 10,
                    depth: 100,
                    modifier: 1,

                    slideShadows: false,
                },

                pagination: {
                    el: '.swiper-pagination',
                    clickable: true,
                },
                navigation: {
                    nextEl: `.swiper-button-prev`,
                    prevEl: `.swiper-button-next`,
                },
            }));
            /*
            var last_swiper = swipers[swipers.length - 1];
            last_swiper.on('transitionEnd', function (d) {
                console.log('transitionEnd');
                set_selected_slide_bigger(d);
            });
            last_swiper.update();*/
            /*
            last_swiper.on('afterInit', function(d) {
                console.log('afterInit');
                set_selected_slide_bigger(d);
            });
            */
            //set_selected_slide_bigger(last_swiper);
        }