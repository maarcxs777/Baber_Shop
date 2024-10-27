let currentIndex = 0;
const items = document.querySelectorAll('.carousel-item');

function showSlide(index) {
  items.forEach((item, i) => {
    item.style.transform = `translateX(${(i - index) * 100}%)`;
  });
}

function nextSlide() {
  currentIndex = (currentIndex + 1) % items.length;
  showSlide(currentIndex);
}

function prevSlide() {
  currentIndex = (currentIndex - 1 + items.length) % items.length;
  showSlide(currentIndex);
}

showSlide(currentIndex);
