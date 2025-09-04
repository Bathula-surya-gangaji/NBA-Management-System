document.addEventListener('DOMContentLoaded', function () {
    const images = ['images/1.jpg', 'images/2.jpeg', 'images/4.jpg']; // Add more image paths as needed
    let currentIndex = 0;

    function changeBackground() {
        document.body.style.setProperty('--background-image', `url(${images[currentIndex]})`);

        currentIndex = (currentIndex + 1) % images.length;
        setTimeout(changeBackground, 5000); // Change image every 5 seconds (adjust as needed)
    }

    changeBackground();
});
