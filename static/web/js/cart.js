function updateCartItemCount() {
    $.ajax({
        url: '/main_context', // Replace with your backend endpoint to get cart item count
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            // Assuming your data format is like: { "count": 5 }
            $('#cart-badge').text(data.count);
        },
        error: function() {
            console.error("Failed to fetch cart item count.");
        }
    });
}

// Call the function when the page loads
$(document).ready(function() {
    updateCartItemCount();
});