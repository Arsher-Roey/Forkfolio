// Global interval variable to control the animation loop
let spinInterval = null;
const frameRate = 750; // The spin speed (milliseconds per frame)

/**
 * Starts the frame-by-frame animation when the mouse hovers over the image.
 * @param {HTMLImageElement} imgElement - The image element being hovered over.
 */
function startSpin(imgElement) {
    // 1. Retrieve the list of image paths from the data attribute on the <img> tag
    // We parse the JSON string back into a JavaScript array.
    const spinImages = JSON.parse(imgElement.dataset.spinImages);

    // Safety check: Clear any existing interval
    if (spinInterval) clearInterval(spinInterval);

    // Start cycling through frames (starting at index 1 to show movement immediately)
    let frameIndex = 1;
    
    // 2. Start the timer loop
    spinInterval = setInterval(() => {
        
        // A. Change the Image: Updates the image source
        imgElement.src = spinImages[frameIndex];
        
        // B. Advance the Frame: Cycle the index (wraps back to 0 after the last image)
        frameIndex = (frameIndex + 1) % spinImages.length;
        
    }, frameRate);
}

/**
 * Stops the animation and resets the image to the front view.
 * @param {HTMLImageElement} imgElement - The image element.
 */
function stopSpin(imgElement) {
    if (spinInterval) clearInterval(spinInterval);
    spinInterval = null;
    
    // Retrieve the image paths again to reset to the front image (index 0)
    const spinImages = JSON.parse(imgElement.dataset.spinImages);
    imgElement.src = spinImages[0];
}
