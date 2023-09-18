// Get the HTML element with the ID "toggle_header"
var toggle_header = document.getElementById('toggle_header');

// Add a click event listener to the "toggle_header" element
toggle_header.addEventListener('click', function () {
    // Get the first header element found in the document
    var header = document.querySelector('header');

    // Check if the header currently has the class "red"
    if (header.classList.contains('red')) {
        // If it has the "red" class, remove it and add the "green" class
        header.classList.remove('red');
        header.classList.add('green');
    }
    else {
        // If it doesn't have the "red" class, remove the "green" class and add the "red" class
        header.classList.remove('green');
        header.classList.add('red');
    }
});
