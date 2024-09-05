// Image thumbnail click functionality
const thumbnails = document.querySelectorAll('.thumbnail');
const mainImage = document.getElementById('main-image');

thumbnails.forEach(thumbnail => {
    thumbnail.addEventListener('click', function() {
        mainImage.src = this.src;
    });
});

// Add to cart button functionality
const addToCartBtn = document.getElementById('add-to-cart-btn');
const quantityInput = document.getElementById('quantity');

addToCartBtn.addEventListener('click', function() {
    const quantity = quantityInput.value;
    alert(`Added ${quantity} item(s) to your cart!`);
});
