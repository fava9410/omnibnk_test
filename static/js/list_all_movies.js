$( document ).ready(function() {

		table_movies = $('#movies').DataTable({
            destroy: true,
            ajax:"/movies/list_all_movies?format=datatables",
            serverSide:true,
            searching: false
        });
});
