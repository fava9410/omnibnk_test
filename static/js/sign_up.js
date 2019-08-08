$( document ).ready(function() {
    var username_exists = true;
    $("#register_submit").prop("disabled",username_exists);
    $("#username").val("")

	  $("#username").on("change keyup paste", function(){

        $.ajax({
            type:"POST",
            cache:false,
            url:"check_username",
            data:{
                "username":$("#username").val()
                },
            success: function (response) {

                if(response == "True"){
                    username_exists = true
                    $("#error_message").text("El propietario ya existe");
                } else {
                    username_exists = false;
                    $("#error_message").text("El propietario no ha sido registrado");
                }

                $("#register_submit").prop("disabled",username_exists);
            }
        });
    });
});
