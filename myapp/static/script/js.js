<!-- Add this script at the bottom of your HTML body or inside a script tag -->
<script>
// JavaScript to make the slider scrollable with mouse wheel and auto-scroll functionality

document.addEventListener('DOMContentLoaded', function() {
    // Grab the slider container element
    const sliderContainer = document.querySelector('#ABdev_main_slider .slider-container');

    // Scroll with mouse wheel
    sliderContainer.addEventListener('wheel', function(e) {
        if (e.deltaY !== 0) {
            // Scroll the container horizontally
            sliderContainer.scrollLeft += e.deltaY;
        }
    });

    // Optional: Auto-scroll the slider every 3 seconds (adjust timing as needed)
    let autoScrollInterval = setInterval(function() {
        sliderContainer.scrollLeft += 300; // Scroll 300px to the right every interval
        if (sliderContainer.scrollLeft + sliderContainer.offsetWidth >= sliderContainer.scrollWidth) {
            // If the end of the slider is reached, reset scroll to the beginning
            sliderContainer.scrollLeft = 0;
        }
    }, 3000); // Adjust the speed by changing the interval time (3000ms = 3 seconds)

    // Optional: Pause auto-scrolling on hover
    sliderContainer.addEventListener('mouseenter', function() {
        clearInterval(autoScrollInterval); // Stop auto-scrolling when mouse enters the slider
    });

    sliderContainer.addEventListener('mouseleave', function() {
        autoScrollInterval = setInterval(function() {
            sliderContainer.scrollLeft += 300; // Continue auto-scrolling
            if (sliderContainer.scrollLeft + sliderContainer.offsetWidth >= sliderContainer.scrollWidth) {
                sliderContainer.scrollLeft = 0; // Reset scroll to the beginning
            }
        }, 3000);
    });

    // Optionally: Enable drag-to-scroll functionality (mouse dragging)
    let isDragging = false;
    let startX, scrollLeft;

    sliderContainer.addEventListener('mousedown', function(e) {
        isDragging = true;
        startX = e.pageX - sliderContainer.offsetLeft;
        scrollLeft = sliderContainer.scrollLeft;
    });

    sliderContainer.addEventListener('mouseleave', function() {
        isDragging = false;
    });

    sliderContainer.addEventListener('mouseup', function() {
        isDragging = false;
    });

    sliderContainer.addEventListener('mousemove', function(e) {
        if (!isDragging) return;
        e.preventDefault();
        const x = e.pageX - sliderContainer.offsetLeft;
        const walk = (x - startX) * 2; // Adjust the speed of dragging (2x faster)
        sliderContainer.scrollLeft = scrollLeft - walk;
    });
});
</script>
