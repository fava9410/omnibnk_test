function add_user_movie(id){
	$.ajax({
			type:"POST",
			cache:false,
			url:"/movies/add_user_movie",
			data: {'movie':id},
			success: function (response) {
				alert("Movie added to your favorite list");
				$("#img_"+id.toString()).hide()
			}
	});
};
