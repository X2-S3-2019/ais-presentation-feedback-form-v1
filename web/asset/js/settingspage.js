var settings = {
    coursesTab: $("#courses-tab"),
    presentationsTab: $("#presntations-tab"),
    studentsTab: $("#students-tab"),
    courseStudentsTab: $("#course-students-tab"),
    container: $("#content"),

    init: function ()
    {
        this.initLoadCourses();
        this.initAddCourseBtn();
    },
    initLoadCourses() {
        var that = this;
        settings.container.load("coursestab.html");
        this.getCourses();
    },
    createCourse() {

        let course_name, course_id;

        $('input').removeClass('is-invalid');
        course_id = $('#course-id').val();
        course_name = $('#course-name').val();

        valid = true;
        if (course_id.length == 0) {
            $('#course-id').addClass('is-invalid')
            valid = false;
        }
        if (course_name.length == 0) {
            $('#course-name').addClass('is-invalid')
            valid = false;
        }
        if (!valid) {
            return false;
        }

        eel.createCourse(course_name, course_id)
        this.getCourses();
    },
    getCourses() {
        $('#courses-table tbody').empty()

        courses = eel.getCourses()(function (courses) {
            courses.forEach(function(row) {
                $('#courses-table tbody').append(
                    '<tr>' +
                        '<th scope="row">' + row[1] + '</th>' +
                        '<td>' + row[2]  +'</td>' +
                        '<td> <button class="link"> remove </button></td>' +
                    '</tr')
            })        
        });
    },


	//initSetFolder: function() {
	//	var that = this;
	//	async function run() {
 //           const res = await eel.setFolder();
 //           if ( res ) {
 //           	that.startBtn.removeClass("disabled");
 //           }
 //       }
	//	this.setfolderBtn.click(function() {
	//		run();
	//	});
	//},
	//initStartBtn: function() {
	//	var that = this;
	//	this.startBtn.click(function() {
	//		if ( that.startBtn.hasClass("disabled") === true ) {
	//			// return;
	//		}
	//		window.location.href = "/accessment.html"
	//	});
 //   },
    initAddCourseBtn: function () {

        //addCourseBtn: $(""),
        //console.log('init add course btn');
        //console.log(this.addCourseBtn);
        $(document).on('click', '#add-course', function () {
            console.log('213123');
            settings.createCourse();
        });
    }
};

$(document).ready(function(){
	settings.init();
});

function reload(confirm_msg) {
    var isconfirm = confirm(confirm_msg);
    if (isconfirm) {
        window.location.reload();
    }
}
eel.expose(reload);

function AisAlert(confirm_msg) {
    alert(confirm_msg);
}
eel.expose(AisAlert);




