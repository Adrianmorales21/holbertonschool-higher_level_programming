// Get the HTML element with the ID "red_header"
var red_header = document.getElementById('red_header');

// Add a click event listener to the "red_header" element
red_header.addEventListener('click', function () {
    // Get the first header element found in the document
    var header = document.querySelector('header');

    // Add the "red" class to the header element
    header.classList.add("red");
});
