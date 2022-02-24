$('#user-status-submit').click(function (){
    var url = $(this).attr('data-url');
    var userId = $(this).attr('data-user-id');
    var csrfToken = $('#django-csrf-token').val();

    $.ajax({
        url:url,
        data:{
            userId: userId,
            csrfmiddlewaretoken:csrfToken
        },
        type:'post',
        success:function (data) {
            if (data.code == 0){
                alert(data.msg);
                window.location.href = window.location.href;
            }else {
                alert(data.msg)
            }
        },
        fail:function (e){
            console.log(e);
        }
    })

});