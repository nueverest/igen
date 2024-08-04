// script.js
function previewFile() {
    const file = document.getElementById('file-input').files[0];
    const reader = new FileReader();
    reader.addEventListener("load", function () {
        // convert image file to base64 string
        document.getElementById('preview-img').src = reader.result;
    }, false);

    if (file) {
        reader.readAsDataURL(file);
    }
}

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

// Function to apply a filter based on the selected image in the filter area
function applyFilter(filterName) {
    const fileInput = document.getElementById('file-input');
    if (fileInput.files.length > 0) {
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);
        formData.append('filter', filterName); // Append the selected filter name

        fetch('/apply-filter', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.url) {
                document.getElementById('preview-img').src = data.url; // Update the preview image
            } else {
                alert('Failed to apply filter.');
            }
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please upload an image first.');
    }
}

// Event listener for filter selection
document.querySelectorAll('.filter-image').forEach(img => {
    img.addEventListener('click', function() {
        const filterName = this.alt; // Assuming alt attribute contains the filter name
        document.querySelectorAll('.filter-image').forEach(img => img.classList.remove('selected'));
        this.classList.add('selected'); // Add 'selected' class for visual feedback
        applyFilter(filterName); // Apply the filter
    });
});
