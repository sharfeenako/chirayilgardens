from .models import CartItem,CartItem_Fertilizer,CartItem_Medicine


def main_context(request):

    cart_items = CartItem.objects.select_related('product').all()
    cart_fertilizers = CartItem_Fertilizer.objects.select_related('fertilizer').all()  # Fetch all cart fertilizer items
    cart_medicines = CartItem_Medicine.objects.select_related('medicine').all()

    total_price_items = sum(float(item.product.price) * item.quantity for item in cart_items)
    total_price_fertilizers = sum(float(item.fertilizer.price) * item.quantity for item in cart_fertilizers)
    total_price_medicines = sum(float(item.medicine.price) * item.quantity for item in cart_medicines)

    
    total_price = total_price_items + total_price_fertilizers + total_price_medicines
    
    return {
        'cart_items': cart_items,
        'cart_fertilizers': cart_fertilizers,
        'cart_medicines': cart_medicines,
        'total_price': total_price,
    }