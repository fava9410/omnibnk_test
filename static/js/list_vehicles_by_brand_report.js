$( document ).ready(function() {

	$("#search").click(function(){
        
		table_vehicles = $('#vehicles').DataTable({
            destroy: true,
            ajax:"/filter_vehicles_by_brand/"+$('#vehicle_brand').val()+"/?format=datatables",
            serverSide:true,
            searching: false
        });
    });
});
