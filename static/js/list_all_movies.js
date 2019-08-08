$( document ).ready(function() {

		table_movies = $('#movies').DataTable({
            destroy: true,
            ajax:"/movies/list_all_movies?format=datatables",
            serverSide:true,
            searching: false,
						"columnDefs": [
            {
                // The `data` parameter refers to the data for the cell.
                // The `rows`argument is an object representing all the data for the current row.
                "render": function ( data, type, row ) {
                    return "<i class='material-icons' onclick=delete_movie('"+data+"') \
										style='cursor: pointer' data-pk='" + data + "' >delete</i> \
										<i class='material-icons' onclick=window.location.replace('/movies/edit_movie/"+data+"') \
										style='cursor: pointer' data-pk='" + data + "' >mode_edit</i>";
                },
                "targets": -1  // -1 is the last column, 0 the first, 1 the second, etc.
            }
        ]
        });
});

function delete_movie(id){
	$.ajax({
			type:"DELETE",
			cache:false,
			url:"/movies/movie_detail/"+id+"/",
			beforeSend: function(xhr) {
				xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'));
			},
			success: function (response) {
				table_movies.clear().draw();
			}
	});
};
