// Get the HTML element with the ID "update_header"
var update_header = document.getElementById('update_header');

// Add a click event listener to the "update_header" element
update_header.addEventListener('click', function () {
    // Get the first header element found in the document
    var header = document.querySelector('header');

    // Update the text content of the header element to "New Header!!!"
    header.textContent = "New Header!!!";
});
