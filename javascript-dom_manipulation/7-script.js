// Get the HTML element with the ID "list_movies"
var list_movies = document.getElementById('list_movies');

// Make a fetch request to the Star Wars API to retrieve a list of movies
fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(function (response) {
        // Check if the response from the API is not OK (e.g., HTTP status code 404)
        if (!response.ok) {
            throw new Error("Error on Network response");
        }
        // If the response is OK, parse it as JSON
        return response.json();
    })
    .then(function (data) {
        console.log(data); // Log the data to the console (optional)

        // Iterate through the list of movies in the data
        data.results.forEach(function (movie) {
            // Create a new list item element
            var movie_title = document.createElement('li');

            // Set the text content of the list item to the movie title
            movie_title.textContent = movie.title;

            // Append the list item to the "list_movies" element
            list_movies.appendChild(movie_title);
        });
    })
    .catch(function (error) {
        // Handle any errors that occur during the fetch operation
        console.error("There was a problem with the fetch operation:", error);
    });
