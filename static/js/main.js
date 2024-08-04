// Function to apply a filter and fetch a generated image
function fetchFilteredImage(filterName) {
    const formData = new FormData();
    formData.append('filter', filterName); // Append the selected filter name

    fetch('/generate-image', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.url) {
            document.getElementById('preview-img').src = data.url; // Update the preview image
        } else {
            alert('Failed to generate filtered image.');
        }
    })
    .catch(error => console.error('Error:', error));
}

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
