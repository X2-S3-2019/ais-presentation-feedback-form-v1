$(document).ready(function(){

    $(window).bind('beforeunload', function(){
        eel.say_hello_py('hello python!');
    });

    /* Prevent right click 
    $(document).on("contextmenu", function () {
        return false;
    }); */

    /* SETTINGS */
    // TODO: Optimize this
    var checkboxAlwaysSetPath = $('#checkboxAlwaysSetPath');

    checkboxAlwaysSetPath.click(function(){
        console.log('clicked checkbox');
        if (this.checked == true) {
            console.log('checked');
            localStorage.setItem('always set path', 'true');
        }
        else {
            console.log('un-checked');
            localStorage.removeItem('always set path');
        }
    });

    var checkboxShowCalculation = $('#showCalculationPopUp');

    checkboxShowCalculation.click(function(){
        console.log('clicked checkbox');
        if (this.checked == true) {
            console.log('checked');
            localStorage.setItem('show calculations', 'true');
        }
        else {
            console.log('un-checked');
            localStorage.removeItem('show calculations');
        }
    });


    $('#btnAddTab').click(function (e) {
        e.preventDefault();
        var nextTabNum = $('#tabs li').length+1;
        var studentID = $('#studentID').val();
        var href = $('<a href="#" tab-num="' + nextTabNum +'" class="far fa-times-circle"></a>');

        // create the tab
        var nextTab = $('<li class="tab"><a href="#tab'+ nextTabNum +'" data-toggle="tab">'+ studentID +'</a> </li>')
        .append(href)
        .appendTo('#tabs');
        
        // create the tab content
        var tabPane = $('<div class="tab-pane" id="tab'+nextTabNum+'">Student ID: ' + studentID + '</div>')
        .appendTo('.tab-content');

        // make the new tab active
        $('#tabs a:first').tab('dispose');
  	    $('#tabs a:last').tab('show');

        // nextTab.click(function (e){
        //     e.preventDefault();
        //     tabPane.show();
        //     $('#tabs li').forEach(element => {
                
        //     });
        // });

        href.click(function (e){
            e.preventDefault();
            $(this).parent().remove();
            nextTab.remove();
            tabPane.remove();
            // Remove corresponding tabPane
        });
        
        $('#studentID').val('');
        // Close popup
        $('#popupAddStudent').modal('toggle');
        
        return false;
    });
});
