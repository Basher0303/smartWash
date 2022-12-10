$(document).ready(function() {
    $('#start-btn').click(function () {
        $(this).attr('disabled', true);
        changeIcon(1);
        request(0);       
    });
});

function request(status) {
    $.ajax({
        type: "post",
        url: "http://localhost:5000/api/status",
        dataType: "json",
        timeout: 600000,
        data: {
            status: status,
        },
        success: function (response) {
            changeIcon(response.status);
            console.log(response.status);
            if(response.status != 5) 
                request(response.status);
        }
    }); 
}

function changeIcon(status) {
    $('.icon').attr('src', `./src/status-${status}.png`);
}
