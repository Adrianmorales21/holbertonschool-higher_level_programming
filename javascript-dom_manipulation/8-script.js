// Wait for the DOM (Document Object Model) to be fully loaded and ready
document.addEventListener("DOMContentLoaded", function () {
    // Get the HTML element with the ID "hello"
    var hello = document.getElementById("hello");

    // Make a fetch request to an external API endpoint that returns a greeting in French
    fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
        .then(function (response) {
            // Check if the response from the API is not OK (e.g., HTTP status code 404)
            if (!response.ok) {
                throw new Error("Error network response");
            }
            // If the response is OK, parse it as JSO
            return response.json();
        })
        .then(function (data) {
            // Update the content of the HTML element with the greeting from the API
            hello.textContent = data.hello;
        })
        .catch(function (error) {
            // Handle any errors that occur during the fetch operation
            console.error("There was a problem with the fetch operation:", error);
        });
});
