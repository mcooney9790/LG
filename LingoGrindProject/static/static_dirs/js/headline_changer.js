var main = function () {


            $(".hidedivs").hide();

            $(".toggler").click(function ()
            {
                $("#" + $(this).attr("id") + "-info").show().siblings('div').hide();
            });


}
$(document).ready(main);