$(document).ready(function()
{
    $("#lista1").als({
        visible_items: 3,
        scrolling_items: 1,
        orientation: "horizontal",
        circular: "yes",
        autoscroll: "no",
        interval: 5000,
        direction: "right"
    });

    //logo hover
    $("#logo_img").hover(function()
    {
        $(this).attr("src","images/als_logo_hover212x110.png");
    },function()
    {
        $(this).attr("src","images/als_logo212x110.png");
    });

    //logo click
    $("#logo_img").click(function()
    {
        location.href = "http://als.musings.it/index.php";
    });

    $("a[href^='http://']").attr("target","_blank");
    $("a[href^='http://als']").attr("target","_self");
});