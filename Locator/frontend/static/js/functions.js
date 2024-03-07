// scripts inside the html should appear after everything

function scrollToSection() {
  document.getElementById('proposalsection').scrollIntoView({
    behavior: 'smooth',
  });
}



document.addEventListener('DOMContentLoaded', function () {
document.querySelectorAll('.heartsection').forEach(function (heartContainer) {
  console.log("added");

  const heartIcon = heartContainer.querySelector('.animated-heart');
  const heartOutline = heartContainer.querySelector('.animated-heart-outline');

  heartIcon.addEventListener('click', function () {
        console.log("yes");

      // Toggle classes for the clicked heartIcon and its corresponding heartOutline
      heartOutline.classList.toggle('heartOutline');
      this.classList.toggle('heartIcon');
  });
});

});


document.addEventListener('DOMContentLoaded', function () {
document.querySelectorAll('.starsection').forEach(function (container) {
  console.log("yes");

  container.addEventListener('click', function(event) {
    const clickedStar = event.target.dataset.star;
    const containerId = container.dataset.containerId;

    const stars = container.querySelectorAll('.starOutline');
    stars.forEach(star => {
      const starNumber = star.dataset.star;

      if (starNumber <= clickedStar) {
        star.classList.add('fas');
        star.classList.remove('far');
      } else {
        star.classList.add('far');
        star.classList.remove('fas');
      }
    });

    console.log(`Clicked Star ${clickedStar} in Container ${containerId}`);
  });
});
});
