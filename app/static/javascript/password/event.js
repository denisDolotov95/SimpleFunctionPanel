
// When the user mouseover the password field, show the message box
$(
    function () {
        $("#password, #password2").mouseover(function () {
            let id = this.id.replace(/[A-Za-z]/g, "");
            $(`#message${id}`).css("display", "block");
        })
    }
);

// When the user mouseout of the password field, hide the message box
$(
    function () {
        $("#password, #password2").mouseout(function () {
            let id = this.id.replace(/[A-Za-z]/g, "");
            $(`#message${id}`).css("display", "none");
        })
    }
);

// When the user starts to type something inside the password field
$(
    function () {        
        $("#password, #password2").on('keyup focus', function () {
            if ($("#password").val() == $("#password2").val()) {
                $("#match").removeClass("invalid");
                $("#match").addClass("valid");
                if ($("#letter").hasClass("valid") && $("#capital").hasClass("valid") &&
                    $("#number").hasClass("valid") && $("#length").hasClass("valid")) {
                        $("#btn-send").removeAttr("disabled");
                    }
            } else {
                $("#match").removeClass("valid");
                $("#match").addClass("invalid");
                $("#btn-send").attr("disabled", true);
            }
        })
    }
);


// When the user starts to type something inside the password field
$(
    function () {        
        $("#password").keyup(function () {
            // Validate lowercase letters
            if (this.value.match(/[a-z]/g)) {
                $("#letter").removeClass("invalid");
                $("#letter").addClass("valid");
            } else {
                $("#letter").removeClass("valid");
                $("#letter").addClass("invalid");
            }

            // Validate capital letters
            if (this.value.match(/[A-Z]/g)) {
                $("#capital").removeClass("invalid");
                $("#capital").addClass("valid");
            } else {
                $("#capital").removeClass("valid");
                $("#capital").addClass("invalid");
            }

            // Validate numbers
            if (this.value.match(/[0-9]/g)) {
                $("#number").removeClass("invalid");
                $("#number").addClass("valid");
            } else {
                $("#number").removeClass("valid");
                $("#number").addClass("invalid");
            }

            // Validate length
            if (this.value.length >= 8) {
                $("#length").removeClass("invalid");
                $("#length").addClass("valid");
            } else {
                $("#length").removeClass("valid");
                $("#length").addClass("invalid");
            }
        })
    }
);