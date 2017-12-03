$(function( $ ){
	/**
	 * Most jQuery.localScroll's settings, actually belong to jQuery.ScrollTo, check it's demo for an example of each option.
	 * @see http://demos.flesler.com/jquery/scrollTo/
	 * You can use EVERY single setting of jQuery.ScrollTo, in the settings hash you send to jQuery.localScroll.
	 */
	
	// The default axis is 'y', but in this demo, I want to scroll both
	// You can modify any default like this
		
	/**
	 * NOTE: I use $.localScroll instead of $('#navigation').localScroll() so I
	 * also affect the >> and << links. I want every link in the page to scroll.
	 */

	$('#navigation').localScroll({
		target: '.content', // could be a selector or a jQuery object too.		
		duration:1500		
	});

	window.addEventListener("hashchange", function () {
		window.scrollTo(window.scrollX, window.scrollY - 50);
	});
});