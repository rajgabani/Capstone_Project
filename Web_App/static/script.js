document.getElementById('imageForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission
    
    // Get input element
    var input = document.getElementById('imageInput');
    
    // Check if a file is selected
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        
        // Read the image file as a data URL
        reader.onload = function(e) {
            var preview = document.getElementById('preview');
            preview.innerHTML = ''; // Clear previous preview if any
            var img = new Image();
            img.src = e.target.result;
            img.width = 200; // Set preview image width
            preview.appendChild(img);
        };
        
        // Load selected image file
        reader.readAsDataURL(input.files[0]);
    }
});