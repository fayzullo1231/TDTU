$(document).ready(function () {
    let totalSlides = $('.slider div').length; // Rasmlar sonini aniqlash

    let slidesToScroll = 1; // Default qiymat

    if (totalSlides > 6 && totalSlides <= 9) {
        slidesToScroll = 2; // 6 tadan oshsa, 2tadan o'tadi
    } else if (totalSlides > 9) {
        slidesToScroll = 3; // 9 tadan oshsa, 3tadan o'tadi
    }

    $('.slider').slick({
        dots: true,
        infinite: true,
        speed: 550,
        slidesToShow: 3, // Har doim 3 ta rasm ko‘rsatadi
        slidesToScroll: slidesToScroll, // Dinamik ravishda belgilangan qiymat
        autoplay: true,
        autoplaySpeed: 2000,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1 // Mobil versiyada 1tadan o'tadi
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
    currentIndex = Math.min(currentIndex + 2, images.length - visibleImages);
    updateImageContainer();
});

prevButton.addEventListener('click', () => {
    currentIndex = Math.max(currentIndex - 1, 0);
    updateImageContainer();
});

const video = document.getElementById('videoPlayer');

function toggleVideo() {
    if (video.paused) {
        video.play();  // Video o'ynatish
    } else {
        video.pause();  // Video pauzaga qo'yish
    }
}

window.onload = function() {
  const logoItems = document.querySelector('.logo_items');
  const logos = logoItems.querySelectorAll('img');

  // Logolarni avtomatik ravishda takrorlash
  logos.forEach(logo => {
    const clonedLogo = logo.cloneNode(true);  // Har bir logoni klonlash
    logoItems.appendChild(clonedLogo);       // Takrorlangan logoni qo‘shish
  });
};
