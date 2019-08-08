$( document ).ready(function() {
	$("#name").val(movie_name)
	$("#director").val(movie_director),
	$("#released_date").val(movie_released_date)
});

function edit_movie(id){

	$.ajax({
			type:"PUT",
			cache:false,
			url:"/movies/movie_detail/"+id+"/",
			beforeSend: function(xhr) {
				xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'));
			},
			data: JSON.stringify({
				name: $("#name").val(),
				director: $("#director").val(),
				released_date: $("#released_date").val()
			}),
			contentType:'application/json',
			dataType: 'json',
			success: function (response) {
				window.location.replace('/movies/all_movies')
			}
	});
};
