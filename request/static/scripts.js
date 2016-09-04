// animated scroll
$(document).ready(function(){
  $('body').scrollspy({target: ".navbar", offset: 50});
  $("#myNavbar a").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
        window.location.hash = hash;
      });
    }
  });
});

// navbar auto height offset
$(document).ready(function(){
    $(".navbar").affix({offset: {top: $("#header").outerHeight(true)} });
});

// parallaxing
var images = [].slice.call(document.querySelectorAll('.parallax'));
function getViewportHeight() {
    var a = document.documentElement.clientHeight, b = window.innerHeight;
    return a < b ? b : a;
}

function getViewportScroll() {
    if(typeof window.scrollY != 'undefined') {
        return window.scrollY;
    }
    if(typeof pageYOffset != 'undefined') {
        return pageYOffset;
    }
    var doc = document.documentElement;
    doc = doc.clientHeight ? doc : document.body;
    return doc.scrollTop;
}

function doParallax() {
    var el, elOffset, elHeight,
        offset = getViewportScroll(),
        vHeight = getViewportHeight();

    for(var i in images) {
        el = images[i];
        elOffset = el.offsetTop;
        elHeight = el.offsetHeight;

        if((elOffset > offset + vHeight) || (elOffset + elHeight < offset)) { continue; }

        el.style.backgroundPosition = '50% '+Math.round((elOffset - offset)*3/8)+'px';
    }
}

Gator(window).on('scroll', doParallax);

// When the user clicks on div, open the popup
function myFunction() {
    var popup = document.getElementById('myPopup');
    popup.classList.toggle('show');
}