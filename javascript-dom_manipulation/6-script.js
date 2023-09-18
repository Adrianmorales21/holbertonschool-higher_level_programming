// Get the HTML element with the ID "character"
var character_element = document.getElementById('character');

// Make a fetch request to the Star Wars API to retrieve information about a character (in this case, character with ID 5)
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(function (response) {
        // Check if the response from the API is not OK (e.g., HTTP status code 404)
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        // If the response is OK, parse it as JSON
        return response.json();
    })
    .then(function (data) {
        // Extract the character's name from the data
        var character_name = data.name;

        // Set the text content of the "character_element" to display the character's name
        character_element.textContent = "Character: " + character_name;
    })
    .catch(function (error) {
        // Handle any errors that occur during the fetch operation
        console.error('There was a problem with the fetch operation:', error);
    });
