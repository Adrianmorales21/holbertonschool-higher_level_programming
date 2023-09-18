// Get the HTML element with the ID "add_item"
var add_item = document.getElementById('add_item');

// Add a click event listener to the "add_item" element
add_item.addEventListener('click', function () {
    // Create a new list item element
    var element = document.createElement('li');

    // Set the text content of the new list item to "Item"
    element.textContent = "Item";

    // Get the first element with the class "my_list"
    var my_list = document.querySelector('.my_list');

    // Append the new list item to the "my_list" element
    my_list.appendChild(element);
});
