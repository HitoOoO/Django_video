var inputNumber = $('#number');
var inputUrl = $('#url');
var videosubInputID = $('#videosub-input-id');

$('.update-btn').click(function(){
    var videosubId = $(this).attr('data-id')
    var videoSubNumber = parseInt($(this).attr('data-number'))
    var videoSubUrl = $(this).attr('data-url')

    inputNumber.val(videoSubNumber);
    inputUrl.val(videoSubUrl);
    videosubInputID.val(videosubId);

});