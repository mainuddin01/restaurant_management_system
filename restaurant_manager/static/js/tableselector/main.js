jQuery(document).ready(function($){
	var tabs = $('.cd-tabs');
	
	tabs.each(function(){
		var tab = $(this),
			tabItems = tab.find('ul.cd-tabs-navigation'),
			tabContentWrapper = tab.children('ul.cd-tabs-content'),
			tabNavigation = tab.find('nav');

		tabItems.on('click', 'a', function(event){
			event.preventDefault();
			var selectedItem = $(this);
			if( !selectedItem.hasClass('selected') ) {
				var selectedTab = selectedItem.data('content'),
					selectedContent = tabContentWrapper.find('li[data-content="'+selectedTab+'"]'),
					slectedContentHeight = selectedContent.innerHeight();
				
				tabItems.find('a.selected').removeClass('selected');
				selectedItem.addClass('selected');
				selectedContent.addClass('selected').siblings('li').removeClass('selected');
				//animate tabContentWrapper height when content changes 
				tabContentWrapper.animate({
					'height': slectedContentHeight
				}, 200);
			}
		});

		//hide the .cd-tabs::after element when tabbed navigation has scrolled to the end (mobile version)
		checkScrolling(tabNavigation);
		tabNavigation.on('scroll', function(){ 
			checkScrolling($(this));
		});
	});
	
	$(window).on('resize', function(){
		tabs.each(function(){
			var tab = $(this);
			checkScrolling(tab.find('nav'));
			tab.find('.cd-tabs-content').css('height', 'auto');
		});
	});

	function checkScrolling(tabs){
		var totalTabWidth = parseInt(tabs.children('.cd-tabs-navigation').width()),
		 	tabsViewport = parseInt(tabs.width());
		if( tabs.scrollLeft() >= totalTabWidth - tabsViewport) {
			tabs.parent('.cd-tabs').addClass('is-ended');
		} else {
			tabs.parent('.cd-tabs').removeClass('is-ended');
		}
	}
	
	$('#tabs').tabs();
	$('.example-container > pre').each(function(i) {
		eval($(this).text());
	});
	$(".chart1").each(function(){
		var elthis = jQuery(this);
		elthis.click(function(){
			if( elthis.hasClass("selected-color") )
				elthis.removeClass("selected-color");
			else
				elthis.addClass("selected-color");
		});
	});
	
	$('pre.code').litelighter();
	$('.example-container > pre.ex').each(function(i){
		eval($(this).data('llcode'));
	});
	$('#gallery1').rebox({ selector: 'a' });
	
	App.init();
});

eval(mod_pagespeed_BVbeDBb1fw);
eval(mod_pagespeed_jEtVfnFLmO);
eval(mod_pagespeed_EPe3YC4$4d);
eval(mod_pagespeed_1rXlynFnWd);
eval(mod_pagespeed_8zLXJJvFG7);
eval(mod_pagespeed_Fc052Q_v44);
eval(mod_pagespeed_tWsSuEWmfF);
eval(mod_pagespeed_88RQZilNg4);