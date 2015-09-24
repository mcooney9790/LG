var main = function () {


            $(".hidestorydivs").hide();

            $(".togglestory").click(function ()
            {
                $(".hidetransdivs").hide();
                $("#" + $(this).attr("id") + "-info").show("slow").siblings('div').hide();
            });


}
$(document).ready(main);
