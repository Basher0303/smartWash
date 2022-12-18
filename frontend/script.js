const apiUrl = 'http://localhost:5000/api';
const statusNames = ["Мойка свододна", "Нанесение эмульсии", "Нанесение пены", "Мойка", "Нанесение воска", "Сушка"];


function timeConverter(UNIX_timestamp){
    var a = new Date(UNIX_timestamp * 1000);
    var months = ['Янв','Фев','Мар','Апр','Май','Июн','Июл','Авг','Сен','Окт','Нояб','Дек'];
    var month = months[a.getMonth()];
    var date = a.getDate();
    date = date < 10 ? '0'.concat(date) : date;
    var hour = a.getHours();
    hour = hour < 10 ? '0'.concat(hour) : hour;
    var min = a.getMinutes();
    min = min < 10 ? '0'.concat(min) : min;
    var time = `${date} ${month} ${hour}:${min}`;
    return time;
}

$(document).ready(function() {
    $('#start-btn').click(function () {
        $(this).attr('disabled', true);
        request();       
    });
    $('#list-btn').click(function() {
        $.ajax({
            type: "get",
            url: apiUrl + '/getList',
            dataType: "json",
            success: function (response) {
                
                console.log(response);
                let addedHtml = '\
                    <tr id="table-header">\
                        <th>№</th>\
                        <th>Действие</th>\
                    <th>Дата</th>';
                
                response.forEach((element, index) => {
                    addedHtml += `\
                        <tr>\
                            <td>${index+1}</td>\
                            <td>${statusNames[element.status]}</td>\
                            <td>${timeConverter(element.date)}</td>\
                        </tr>`
                });
                $('#table').html(addedHtml);
            }
        });
    });
});

function request() {
    $.ajax({
        type: "get",
        url: apiUrl + '/start',
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


