$('#comment-submit').click(function () {
    var content = $('#comment-content').val();
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    var videoId = $(this).attr('data-video-id');
    var userId = $(this).attr('data-user-id');
    var url = $(this).attr('data-url');

    if (!content) {
        alert('���۲���Ϊ��!');
        return;
    }

    $.ajax({
        url: url,
        data: {
            content: content,
            videoId: videoId,
            userId: userId,
            csrfmiddlewaretoken: csrfToken
        },
        type: 'post',
        success: function (data) {
            console.log(data)
        },
        fail: function (e) {
            console.log(e);
        }
    });
});