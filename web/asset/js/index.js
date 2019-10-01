var mainpage = {
	startBtn: $("#start"),
	setfolderBtn: $("#setfolder"),

    init: function () {
		this.initSetFolder();
        this.initStartBtn();
	},
	initSetFolder: function() {
		var that = this;
		async function run() {
            const res = await eel.setFolder();
            if ( res ) {
            	that.startBtn.removeClass("disabled");
            }
        }
		this.setfolderBtn.click(function() {
			run();
		});
	},
	initStartBtn: function() {
		var that = this;
		this.startBtn.click(function() {
			if ( that.startBtn.hasClass("disabled") === true ) {
				// return;
			}
			window.location.href = "/accessment.html"
		});
    },
    getCourses: function () {
        courses = eel.getCourses()(function (courses) {
            console.log(courses);
            courses.forEach(function (row) {
                $('#courses-assess').append(
                    '<option value=' + row[1] + '>' +
                    row[2] +
                    '</option>'
                )
            })
        });
    },
    getPresentations: function () {
        let course_id = $('#courses-assess').val();
        presentations = eel.getPresentations(course_id)(function (presentations) {
            presentations.forEach(function (row) {
                $('#presentations-assess').append(
                    '<option value=' + row[0] + '>' +
                    rowp[1] + ' ' + row[2] + 
                    '</option>'
                )
            })
        });
    }
};

var assess = {
	data: {
		"content": {
			"focus": 0,
			"organization": 0,
			"visual_aids": 0,
			"QA": 0,
		},
		"lang": {
			"eye_contact": 0,
			"enthusiasm": 0,
			"elocution": 0,
		},
		"technical": {
			"knowledge": 0,
			"research": 0,
			"ideas": 0,
			"argument": 0,
			"questions": 0,
		}
	},
	header: {
		"sname": "",
		"sid": "",
		"topic": "",
	},
	student_name: $("#student_name"),
	student_id: $("#student_id"),
	topic: $("#topic"),
	saveBtn: $("#save"),
	generateBtn: $("#generate"),
	init: function() {
		this.initialSelect();
		this.initalHeader();
        this.initialSave();
        mainpage.getCourses();
        mainpage.getPresentations();
	},
	initialSelect: function() {
		var that = this;
		$('td').click(function(e){
			if ( that.checkHeader() === false ) {
				return;
			}
			$(e.target).parent().removeClass("table-danger");
			var score = $(e.target).attr('data-score');
			var type = $(e.target).attr('data-type');
			var classname = "";
			if ( score == 4 ) {
				classname = "table-success";
			} else if ( score == 3 ) {
				classname = "table-primary";
			} else if ( score == 2 ) {
				classname = "table-warning";
			} else if ( score == 1 ) {
				classname = "table-danger";
			}
			$('td[data-type="' + type + '"]').removeClass();
			$(e.target).addClass(classname);
			var tmp = type.split('.')
			that.data[tmp[0]][tmp[1]] = score;
		});
	},
	initalHeader: function() {
		var that = this;
		this.student_name.blur(function(){
			that.checkHeader();
		});
		this.student_id.blur(function(){
			that.checkHeader();
		});
		this.topic.blur(function(){
			that.checkHeader();
		});
	},
	initialSave: function() {
		var that = this;
		this.saveBtn.click(function() {
			if ( that.checkHeader() ) {
				var ret = that.checkOption();
				if ( ret ) {
					eel.generdate_word(JSON.stringify(that.data), JSON.stringify(that.header));
				}
			}
		});
	},
	checkHeader: function() {
		if ( this.student_name.val() == "" ) {
			this.student_name.addClass("is-invalid");
			this.student_name.focus();
			return false;
		} else {
			this.student_name.removeClass("is-invalid");
			this.header.sname = this.student_name.val();
		}
		if ( this.student_id.val() == "" ) {
			this.student_id.addClass("is-invalid");
			this.student_id.focus();
			return false;
		} else {
			this.student_id.removeClass("is-invalid");
			this.header.sid = this.student_id.val();
		}
		if ( this.topic.val() == "" ) {
			this.topic.addClass("is-invalid");
			this.topic.focus();
			return false;
		} else {
			this.topic.removeClass("is-invalid");
			this.header.topic = this.topic.val();
		}
		return true;
	},
	checkOption: function() {
		var that = this;
		for (category in that.data ) {
			for ( subcate in that.data[category] ) {
				if ( that.data[category][subcate] == 0 ) {
					var tmp = $('tr[data-type="' + category + '.' + subcate + '"]');
					tmp.addClass("table-danger");
					$('body, html').animate({
						scrollTop: tmp.offset().top
					});
					that.generateBtn.addClass("disabled");
					return false;
				}
			}
		}
		that.generateBtn.removeClass("disabled");
		return true;
	},
}

$(document).ready(function(){
	assess.init();
    //start.init();
});


eel.expose(say_hello_js);               // Expose this function to Python
function say_hello_js(x) {
    console.log("Hello from " + x);
}
say_hello_js("Javascript World!");
//eel.say_hello_py("Javascript World!");  // Call a Python function


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




