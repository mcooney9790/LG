var main = function () {


            $(".hidetransdivs").hide();

            $(".toggletrans").toggle(function ()
            {
                $("#" + $(this).attr("id") + "-info").show("slow").siblings('div').hide();
            },function()
            {
                $("#" + $(this).attr("id") + "-info").hide("slow")
            });


}
$(document).ready(main);
