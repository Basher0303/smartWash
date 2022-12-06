$(document).ready(function() {
    $('#start-btn').click(function () {
        $.ajax({
            type: "get",
            url: "https://jsonplaceholder.typicode.com/posts",
            dataType: "json",
            success: function (response) {
                console.log(response);
            }
        });        
    });
});