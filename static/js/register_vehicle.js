$( document ).ready(function() {
    var vehicle_exists = true;
    var owner_exists = true;
    var disabled_submit = true;
    
    $("#license_plate").val("");
    $("#owner").val("");

	$("#license_plate").on("change keyup paste", function(){

        $.ajax({
            type:"POST",
            cache:false,
            url:"check_license_plate",
            data:{"license_plate":$("#license_plate").val()},
            success: function (response) {

                if(response == "True"){
                    vehicle_exists = true;
                    $("#error_message").text("La placa ya existe");
                } else {
                    vehicle_exists = false;
                    $("#error_message").text("La placa no existe");
                }

                disabled_submit = validate_disabled_submit(vehicle_exists, owner_exists, disabled_submit)

                $("#vehicle_submit").prop("disabled",disabled_submit);
            }
        });
    });

    
    $("#owner").on("change keyup paste", function(){

        $.ajax({
            type:"POST",
            cache:false,
            url:"check_owner",
            data:{
                "number_document":$("#owner").val()
                },
            success: function (response) {

                if(response == "True"){
                    owner_exists = false
                    $("#error_message_owner").text("El propietario fue seleccionado exitosamente");
                } else {
                    owner_exists = true;
                    $("#error_message_owner").text("El propietario no ha sido registrado");
                }

                disabled_submit = validate_disabled_submit(vehicle_exists, owner_exists, disabled_submit)

                $("#vehicle_submit").prop("disabled",disabled_submit);
            }
        });
    });

});

function validate_disabled_submit(vehicle_exists, owner_exists, disabled_submit){
    if(vehicle_exists == owner_exists && vehicle_exists == false){
        disabled_submit = false;
    }
    else{
        disabled_submit = true;
    }
    return disabled_submit;
}