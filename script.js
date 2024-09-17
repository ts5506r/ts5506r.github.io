document.querySelectorAll('.product-card').forEach(card => {
    card.addEventListener('click', function() {
        const productId = this.getAttribute('data-product-id');
        window.location.href = `product-details.html?product_id=${productId}`;
    });
});

// Add to cart button functionality
const addToCartBtn = document.getElementById('add-to-cart-btn');
const quantityInput = document.getElementById('quantity');

addToCartBtn.addEventListener('click', function() {
    const quantity = quantityInput.value;
    alert(`Added ${quantity} item(s) to your cart!`);
});