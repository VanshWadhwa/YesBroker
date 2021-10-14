jQuery('document').ready(function(){

    //Function based in http://stackoverflow.com/questions/487073/check-if-element-is-visible-after-scrolling
    //Scott Dowding is solution
  function isScrolledIntoView(elem)
  {
      var docViewTop = $(window).scrollTop();
      var docViewBottom = docViewTop + $(window).height();
  
      var elemTop = $(elem).offset().top;
      var elemBottom = elemTop + $(elem).height();
  
      return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
  }
  
    jQuery.fn.minimize = function(){
       this.removeClass("maximize");
       this.addClass("minimize");
    };
    
    jQuery.fn.maximize = function(){
       this.removeClass("minimize");
       this.addClass("maximize");
    };
    
    //Maximize the first card after load
    jQuery('.card').eq(0).maximize();
    
   jQuery(window).on("scroll", function() {
     
    jQuery('.card').each(function(i) {
      
     if(isScrolledIntoView( jQuery('.card').eq(i) ) ) {
        jQuery('.card').eq(i).maximize();
     }else{
        jQuery('.card').eq(i).minimize();
     }
                         
    }); 
   });
    
  });