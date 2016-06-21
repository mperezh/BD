$(document).ready(function(){

    $(".button-collapse").sideNav();
    $('.parallax').parallax();

});

$(window).load(function(){

  $('#preloader').fadeOut('slow');
  $('body').css({'overflow':'visible'});

});

var previousScroll = 0,
    headerOrgOffset = $('#header').height();

$('#header-wrap').height($('#header').height());

$(window).scroll(function () {
    var currentScroll = $(this).scrollTop();
    if (currentScroll > headerOrgOffset) {
        if (currentScroll > previousScroll) {
            $('#header-wrap').slideUp('slow');
            $('nav').css({'background':'rgba(0, 0, 0, 0)'});
        } else {
            $('#header-wrap').slideDown('slow');
            $('nav').css({'background':'#000'});
        }
    } else {
            $('#header-wrap').slideDown('slow');
            $('nav').css({'background':'rgba(0, 0, 0, 0)'});
    }
    previousScroll = currentScroll;
});
