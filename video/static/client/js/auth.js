$('#regist-submit').click(function(){
    var username = $('#username').val();
    var password = $('#password').val();
    var url = $(this).attr('data-url');
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();

    if(!username ||!password) {
        alert('缺少必要字段');
        return;
    }

    $.ajax({
        url: url,
        type: 'post',
        data: {
            username: username,
            password: password,
            csrfmiddlewaretoken: csrfToken
        },
        success: function (data){
            alert(data.msg)
        },
        fail: function (e){
            console.log('error:%s', e)
        }
    });

});

$('#login-submit').click(function () {
    var username = $('#username').val();
    var password = $('#password').val();
    var url = $(this).attr('data-url');
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();

    if(!username ||!password) {
        alert('缺少必要字段');
        return;
    }

    $.ajax({
        url: url,
        type: 'post',
        data: {
            username: username,
            password: password,
            csrfmiddlewaretoken: csrfToken
        },
        success: function (data){
            if (data.code) {
                alert(data.msg)
            } else {
                window.location.href = '/client/video/ex';
            }
        },
        fail: function (e){
            console.log('error:%s', e)
        }
    });
});