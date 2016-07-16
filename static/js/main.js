$(document).ready(function(){

    $(".button-collapse").sideNav();
    $('.parallax').parallax();
    $('.modal-trigger').leanModal();
    
    var owl = $("#owl-demo");
    
    owl.owlCarousel({
        autoPlay: true,
        items: 2, //10 items above 1000px browser width
        itemsDesktop: [1000, 2], //5 items between 1000px and 901px
        itemsDesktopSmall: [900, 2], // betweem 900px and 601px
        itemsTablet: [600, 2], //2 items between 600 and 0
        itemsMobile: [479,1] // itemsMobile disabled - inherit from itemsTablet option
    });
    
    // Custom Navigation Events
    $(".next").click(function() {
        owl.trigger('owl.next');
    })
    $(".prev").click(function() {
        owl.trigger('owl.prev');
    })
});

