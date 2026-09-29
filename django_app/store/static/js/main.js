let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelectorAll(".hero-slide");

    if (!slides.length) {
        return;
    }

    currentSlide = (index + slides.length) % slides.length;

    slides.forEach((slide, i) => {
        slide.classList.toggle("active", i === currentSlide);
    });
}

function changeSlide(direction) {
    showSlide(currentSlide + direction);
}

document.addEventListener("DOMContentLoaded", () => {
    showSlide(0);

    setInterval(() => {
        changeSlide(1);
    }, 5000);
});
