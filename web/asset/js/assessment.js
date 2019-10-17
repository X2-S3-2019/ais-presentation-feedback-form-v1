$(document).ready(function(){

    $('#popupAddStudent').modal('show');

    $('#btnAssess').click(function (e) {
    e.preventDefault();

  // Check required fields
    var studentID = $('#student_id').val();
    var studentName = $('#student_name').val();
    var course = $('#courses-assess').val();
    var topic = $('#presentations-assess option:selected').text();

    if(isEmptyOrSpaces(studentID)){
        $('#student_id').addClass('is-invalid');
    } else if(isEmptyOrSpaces(studentName)){
        $('#student_name').addClass('is-invalid');
    } else {
        $('.studentNameHolder').html(studentName);
        $('.studentIDHolder').html(studentID);
        $('.courseNameHolder').html(course);
        $('.topicNameHolder').html(topic);
   // Close popup
    $('#popupAddStudent').modal('toggle');
    }
    });

    // Floating Menu Events
    $('.items-wrapper a').click(function(e) {
        $('#popupConfirmExit').modal('show');

        if($(this).attr('title') == "Setup"){
            $('#popupExitButton').click(function (e){
                location.href = "coursesettings.html";
            });
        } else if(($(this).attr('title') == "Main Menu")){
            $('#popupExitButton').click(function (e){
                location.href = "main.html";
            });
        } else if(($(this).attr('title') == "How to Use")){
            $('#popupExitButton').click(function (e){
                location.href = "splash.html";
            });
        }
    });
});

function isEmptyOrSpaces(str){
    return str === null || str.match(/^ *$/) !== null;
}