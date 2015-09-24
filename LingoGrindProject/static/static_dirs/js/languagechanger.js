var main = function () {


            $(".hidedivs").hide();

            $(".toggler").click(function ()
            {
                $(".hidestorydivs").hide();
                $(".hidetransdivs").hide();
                $("#" + $(this).attr("id") + "-info").show("slow").siblings('div').hide();

            });


            $(".header-divs").hide()


            $(".header-button").click(function ()
            {
                $("#" + $(this).attr("id") + "-info").show("slow").siblings('div').hide("slow");

            });


            $(".backbutton").click( function()
            {

                $(this).parent().hide("slow");

            });




            (function() {  

            var tagline = $(".tagline"); 
            var taglineIndex = -1; 
              
            function showNextTagline() { 
                ++taglineIndex; 
                tagline.eq(taglineIndex % tagline.length) 
                .fadeIn(2000) 
                .delay(2000) 
                .fadeOut(2000, showNextTagline); 

                }
                      

            showNextTagline();      })();



}
$(document).ready(main);
