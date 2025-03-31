$(document).ready(function () {
    $('.slider').slick({
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 3,
        autoplay: true,
        autoplaySpeed: 2000,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1
                }
            }
        ]
    });
});


const imageContainer = document.querySelector('.image-container');
const prevButton = document.querySelector('.carousel-btn.prev');
const nextButton = document.querySelector('.carousel-btn.next');
const images = document.querySelectorAll('.image-container img');
const imageWidth = images[0].clientWidth;
const visibleImages = 3;
let currentIndex = 0;

imageContainer.style.width = `${imageWidth * images.length}px`;

function updateImageContainer() {
    let translateX = -currentIndex * imageWidth;
    imageContainer.style.transform = `translateX(${translateX}px)`;
}

nextButton.addEventListener('click', () => {
    currentIndex = Math.min(currentIndex + 3, images.length - visibleImages);
    updateImageContainer();
});

prevButton.addEventListener('click', () => {
    currentIndex = Math.max(currentIndex - 3, 0);
    updateImageContainer();
});