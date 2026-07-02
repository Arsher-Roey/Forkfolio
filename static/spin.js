const frameRate = 750; // The spin speed (milliseconds per frame)

/**
 * Starts the frame-by-frame animation automatically.
 * @param {HTMLImageElement} imgElement - The image element to animate.
 */
function startAutoSpin(imgElement) {
    // Retrieve the list of image paths from the data attribute
    const spinImages = JSON.parse(imgElement.dataset.spinImages);

    // Safety check: Clear any existing interval attached specifically to this image
    if (imgElement.spinInterval) {
        clearInterval(imgElement.spinInterval);
    }

    // Start cycling through frames
    let frameIndex = 1;
    
    // Attach the interval directly to the image object to prevent global variable clashes
    imgElement.spinInterval = setInterval(() => {
        // Change the Image source
        imgElement.src = spinImages[frameIndex];
        
        // Advance the Frame and loop back to 0
        frameIndex = (frameIndex + 1) % spinImages.length;
        
    }, frameRate);
}

// Listen for the HTML to finish loading, then trigger the animations
document.addEventListener('DOMContentLoaded', () => {
    // Find every single image tag on the page that contains the 'data-spin-images' attribute
    const autoSpinImages = document.querySelectorAll('img[data-spin-images]');

    // Loop through the list and start the spin for each one automatically
    autoSpinImages.forEach(img => {
        startAutoSpin(img);
    });
});
