$(document).ready(function() {
    $('#start-btn').click(function () {
        request(1);       
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
            console.log(response.status);
            if(status != 5) 
                request(response.status);
        }
    }); 
}