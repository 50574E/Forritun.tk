$(document).ready(function(){
	var isRed = false;
	var c1 = "#253a5f";
	var c2 = "#df0000";
	$(".bgColor").click(function(){
		isRed = !isRed;
		if(isRed){
			$("body").css("background",c2);
			$("a").css("color",c2);
			$(".bgColor").css("background",c1);
		}else{
			$("body").css("background",c1);
			$("a").css("color",c1);
			$(".bgColor").css("background",c2);
		}
	});

	var colorHover = function(sel,bg,over){
		var a = c1; var b = c2;
		if(!over){var t = a; a = b; b = t;}
		if(isRed) $(sel).css(bg,a);
		else $(sel).css(bg,b);
	};

	$(".bgColor").mouseover(function(){colorHover(this,"background",true);});
	$("a").mouseover(function(){colorHover(this,"color",true);});
	$(".bgColor").mouseout(function(){colorHover(this,"background",false);});
	$("a").mouseout(function(){colorHover(this,"color",false);});

});