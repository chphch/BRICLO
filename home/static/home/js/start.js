$(".checkbox").click(function(){
	$(this).toggleClass("checkbox_toggle");
});
$("#button_next_1").click(function(){
	$(".page1").css("display","none")
	$(".page2").css("display","block");
});

$("#button_next_2").click(function(){
	$(".page2").css("display","none")
	$(".page3").css("display","block");
});
