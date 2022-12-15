$(document).ready(function() {
    $('#start-btn').click(function () {
        $(this).attr('disabled', true);
        request();       
    });
});

function request() {
    $.ajax({
        type: "get",
        url: "http://localhost:5000/api/start",
        dataType: "json",
        timeout: 600000,
        success: function (response) {
            changeIcon(response.status);
            changeStatusName(response.statusName);
            if(response.status == 0) {
                $('#start-btn').removeAttr('disabled');
                $(`.step-list li`).removeClass('active');
                $(`.step-list li`).removeClass('progress');
            }
            else {
                request(response.status);
                if(response.status > 1){
                    $(`.step-list li:nth-child(${response.status-1})`).removeClass('progress');       
                    $(`.step-list li:nth-child(${response.status-1})`).addClass('active');       
                }         
                $(`.step-list li:nth-child(${response.status})`).addClass('progress');
            }
        }   
    }); 
}

function changeIcon(status) {
    $('.icon').attr('src', `./src/status-${status}.png`);
}

function changeStatusName(name) {
    $('#name-status').text(name);
}


