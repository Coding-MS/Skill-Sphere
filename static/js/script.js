// function that enables the burger menu to be toggled //

function toggleMenu() {
    var menu = document.getElementById("menu");
    menu.classList.toggle("show");
  }


// Function for carousel // 
$(document).ready(function(){
  $('.testimonial-carousel').slick({
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
  });
});
