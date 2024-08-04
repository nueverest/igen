// Assuming there's a form with id 'imageForm' and an input with id 'user_input'
document.getElementById('imageForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting the traditional way

    let userInput = document.getElementById('user_input').value;

    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `user_input=${encodeURIComponent(userInput)}`
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response data, i.e., display images
        const imagesContainer = document.getElementById('imagesContainer');
        imagesContainer.innerHTML = '';  // Clear previous images

        data.images.forEach(imageUrl => {
            let imgElement = document.createElement('img');
            imgElement.src = imageUrl;
            imagesContainer.appendChild(imgElement);
        });
    })
    .catch(error => console.log('Error:', error));
});


// Function to save the generated image
function saveImage() {
    const imgSrc = document.getElementById('preview-img').src;
    if (imgSrc) {
        const a = document.createElement('a');
        a.href = imgSrc;
        a.download = "styled-image.png"; // Set the file name for download
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    } else {
        alert("No image to save!");
    }
}

// Event listener for filter selection
document.querySelectorAll('.filter-image').forEach(img => {
    img.addEventListener('click', function() {
        const filterName = this.alt; // Assuming alt attribute contains the filter name
        document.querySelectorAll('.filter-image').forEach(img => img.classList.remove('selected'));
        this.classList.add('selected'); // Add 'selected' class for visual feedback
        fetchFilteredImage(filterName); // Fetch and display the image with the applied filter
    });
});
