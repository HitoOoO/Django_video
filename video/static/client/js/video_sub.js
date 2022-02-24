var ajaxCommentShow = $('#ajax-comment-show');


$('#comment-submit').click(function (){
    var content = $('#comment-content').val();
    var csrfToken = $('#django-csrf-token').val();
    var videoId = $(this).attr('data-video-id');
    var userId = $(this).attr('data-user-id');
    var url = $(this).attr('data-url');


    if (!content) {
        alert('评论不能为空!');
        return;
    };

    $.ajax({
        url: url,
        data: {
            content: content,
            videoId: videoId,
            userId: userId,
            csrfmiddlewaretoken: csrfToken
        },
        type: 'post',
        success: function(data){
            if (data.code == 0){
                ajaxCommentShow.html('');
                var _data=data.data.comment;
                var content= _data.content;
                var username = _data.username;
                var str = content + '' + username;
                ajaxCommentShow.html(str);
            }
        },
        fail: function(e) {
            console.log(e);
        }
    });
});