$( document ).ready(function() {
    var owner_exists = true;
    $("#owner_submit").prop("disabled",owner_exists);
    $("#number_document").val("")

	$("#number_document").on("change keyup paste", function(){

        $.ajax({
            type:"POST",
            cache:false,
            url:"check_owner",
            data:{
                "number_document":$("#number_document").val()
                },
            success: function (response) {

                if(response == "True"){
                    owner_exists = true
                    $("#error_message").text("El propietario ya existe");
                } else {
                    owner_exists = false;
                    $("#error_message").text("El propietario no ha sido registrado");
                }

                $("#owner_submit").prop("disabled",owner_exists);
            }
        });
    });
});
