$(document).ready(function(){
	if($('html').hasClass('svg')){
		$( ".switch-svg" ).each(function() {
			var targetClass = this;
		  	changeForSvg(targetClass);
		});
	}

	$(document).on('open', '.remodal', function () {
    console.log('open');
});

$(document).on('opened', '.remodal', function () {
    console.log('opened');
});

$(document).on('close', '.remodal', function () {
    console.log('close');
});

$(document).on('closed', '.remodal', function () {
    console.log('closed');
});

$(document).on('confirm', '.remodal', function () {
    console.log('confirm');
});

$(document).on('cancel', '.remodal', function () {
    console.log('cancel');
});


});

function changeForSvg(oneImage){
	var srcInitial = $(oneImage).attr('src');
	var nouvelleSrc = srcInitial.replace("png","svg");
	$(oneImage).attr('src',nouvelleSrc);
}