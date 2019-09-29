var start = {
	startBtn: $("#start"),
	settingsBtn: $("#settings"),
    init: function () {
        this.initSettingsBtn();
		this.initStartBtn();
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
    initSettingsBtn: function () {
        var that = this;
        this.settingsBtn.on('click', function () {
            console.log('123123');
            window.location.href = "coursesettings.html"
        });
    }
};

$(document).ready(function () {
    start.init();
});
