document.addEventListener("DOMContentLoaded", function () {
    // Initialize Bootstrap Carousel with custom interval
    let carousel = document.querySelector("#serviceCarousel");
    let carouselInstance = new bootstrap.Carousel(carousel, {
        interval: 3000, // Auto-slide every 3 seconds
        ride: "carousel",
        pause: false
    });

    // Add smooth fade effect when transitioning
    let carouselItems = document.querySelectorAll(".carousel-item");
    carousel.addEventListener("slide.bs.carousel", function () {
        carouselItems.forEach((item) => {
            item.classList.remove("active");
            setTimeout(() => item.classList.add("active"), 500); // Delay for smooth transition
        });
    });
});
