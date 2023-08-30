from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib import messages
from .forms import InquiryForm



def index(request) :
    context={

        'is_index' : True,
        'banner' : Banner.objects.all()[:1],
        'products' : Product.objects.all()[:4],
        'category' : ProductCategory.objects.all(),
        'testimonial' : Testimonial.objects.all(),
        'gallery' : Gallery.objects.all()[:3],
        'updates' : Update.objects.all()[:3],

    }
    if request.method == "POST" :
        print(request.POST)
        print('hi'*100)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact (
            name = name,
            email = email,
            phone = phone,
            message=message
        )
        contact.save()
        messages.success(request,"succsessfully saved")
        return redirect('web:contact')

    return render(request,"web/index.html",context)


def about(request) :
    context={

        'is_about' : True,
        'testimonial' : Testimonial.objects.all(),
        'faq' : Faq.objects.all()[ : 3],


    }
    return render(request,"web/about-us.html",context)


def shop(request) :
    context={

        'is_shop' : True,
        'category' : ProductCategory.objects.all(),
        'catalogue' : Catalogue.objects.all()[:1],

    }
    return render(request, "web/shop.html", context)

def shop_single(request, id) :
    product_category = ProductCategory.objects.get(id=id)
    productsingle = Product.objects.filter(product_category=product_category)
    paginator = Paginator(productsingle, 8)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    context = {
        'productsingle' :  paged_product,
        "start_index" :  paged_product.start_index(),
        "end_index" :  paged_product.end_index(),

        "pagination" :  paged_product.paginator,
    }
    return render(request, "web/shop-single.html", context)


def shop_detail(request, id) :
    product = Product.objects.get(id=id)
    packages = DetailProduct.objects.filter(product_name=product)
    form = InquiryForm()
    form.fields['fertilizer_package'].queryset = Fertilizer.objects.filter(product_name=product)
    form.fields['medicine_package'].queryset = Medicine.objects.filter(product_name=product)
    form.fields['product'].initial = product.product_name
    context = {
        'products' :  product,
        'packages': packages,
        'video' :  Video.objects.filter(product_name=product),
        'productdetail' :  DetailProduct.objects.filter(product_name=product),
        'fertilizer' :  Fertilizer.objects.filter(product_name=product),
        'medicine' :  Medicine.objects.filter(product_name=product),
        'form' :  form,  # Pass the form to the context here
    }

    return render(request, "web/shop-detail.html", context)



def substance(request) :
    context={
    'is_fertilizer'  : True,
    'fertilizer' : Fertilizer.objects.all(),
    'medicine' : Medicine.objects.all(),
    }
    return render(request,"web/substance.html",context)

def fertilizer_detail(request,id) :
    fertilizer = Fertilizer.objects.get(id=id)
    packages = Package.objects.filter(name=fertilizer)
    context={
    'is_fertilizer'  : True,
    'fertilizer' : fertilizer,
    'packages': packages,

    }
    return render(request,"web/fertilizer-detail.html",context)


def medicine_detail(request,id) :
    medicine = Medicine.objects.get(id=id)
    packages = Quantity.objects.filter(name=medicine)

    context={
    'is_fertilizer'  : True,
    'medicine' : medicine,
    'packages': packages,

    }
    return render(request,"web/medicine-detail.html",context)



def gallery(request) :

    context={
        'is_gallery' : True,
        'gallery' : Gallery.objects.all(),
    }
    return render(request,"web/project.html",context)

def updates(request) :
    context={

        'is_updates' : True,
        'updates' : Update.objects.all()
    }
    return render(request,"web/blog.html",context)

def update_detail(request,id) :
    updates = Update.objects.get(id=id)
    context={
        'is_updates' : True,
        'updates' : updates

    }
    return render(request,"web/blog-single.html",context)

def guide(request) :
    context={

        'is_guide' : True,
        'faq' : Faq.objects.all(),
    }
    return render(request,"web/guide.html",context)




def contact(request) :
    context={

        'is_connect' : True,
    }

    if request.method == "POST" :
        print(request.POST)
        print('hi'*100)
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        contact = Contact (
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        contact.save()
        messages.success(request,"succsessfully saved")
        return redirect('web:contact')
    return render(request,"web/contact-us.html",context)


def cart_add(request, id):
    product = DetailProduct.objects.get(id=id)
  # Assuming DetailProduct is the correct model
    
    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(product=product)
    
    # Increment the quantity if the item already exists in the cart
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("web:cart")

def cart_fertlizer(request, id):
    fertilizer = Package.objects.get(id=id)
  # Assuming DetailProduct is the correct model
    
    # Check if the product is already in the cart
    cart_item, created = CartItem_Fertilizer.objects.get_or_create(fertilizer =fertilizer )
    
    # Increment the quantity if the item already exists in the cart
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("web:cart")

def cart_medicine(request, id):
    medicine = Quantity.objects.get(id=id)
  # Assuming DetailProduct is the correct model
    
    # Check if the product is already in the cart
    cart_item, created = CartItem_Medicine.objects.get_or_create(medicine =medicine )
    
    # Increment the quantity if the item already exists in the cart
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("web:cart")



def item_clear(request, id):
    try:
        cart_item = CartItem.objects.get(product_id=id)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass

    try:
        cart_fertilizer = CartItem_Fertilizer.objects.get(fertilizer_id=id)
        cart_fertilizer.delete()
    except CartItem_Fertilizer.DoesNotExist:
        pass

    try:
        cart_medicine = CartItem_Medicine.objects.get(medicine_id=id)
        cart_medicine.delete()
    except CartItem_Medicine.DoesNotExist:
        pass
    
    return redirect("web:cart")
def item_increment(request, id):
    try:
        cart_item = CartItem.objects.get(product_id=id)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = None
    
    try:
        cart_medicine = CartItem_Medicine.objects.get(medicine_id=id)
        cart_medicine.quantity += 1
        cart_medicine.save()
    except CartItem_Medicine.DoesNotExist:
        cart_medicine = None
    
    try:
        cart_fertilizer = CartItem_Fertilizer.objects.get(fertilizer_id=id)
        cart_fertilizer.quantity += 1
        cart_fertilizer.save()
    except CartItem_Fertilizer.DoesNotExist:
        cart_fertilizer = None
    
    return redirect("web:cart")

def item_decrement(request, id):
    try:
        cart_item = CartItem.objects.get(product_id=id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        cart_item = None
    
    try:
        cart_medicine = CartItem_Medicine.objects.get(medicine_id=id)
        if cart_medicine.quantity > 1:
            cart_medicine.quantity -= 1
            cart_medicine.save()
        else:
            cart_medicine.delete()
    except CartItem_Medicine.DoesNotExist:
        cart_medicine = None
    
    try:
        cart_fertilizer = CartItem_Fertilizer.objects.get(fertilizer_id=id)
        if cart_fertilizer.quantity > 1:
            cart_fertilizer.quantity -= 1
            cart_fertilizer.save()
        else:
            cart_fertilizer.delete()
    except CartItem_Fertilizer.DoesNotExist:
        cart_fertilizer = None
    
    return redirect("web:cart")



def cart_clear(request):
    CartItem.objects.all().delete()
    CartItem_Fertilizer.objects.all().delete()
    CartItem_Medicine.objects.all().delete()

    return redirect("web:cart")

def cart(request):
    cart_items = CartItem.objects.select_related('product').all()
    cart_fertilizers = CartItem_Fertilizer.objects.select_related('fertilizer').all()
    cart_medicines = CartItem_Medicine.objects.select_related('medicine').all()  # Fetch all cart fertilizer items

    
    total_price = 0
    
    for cart_item in cart_items:
        product = cart_item.product
        try:
            price = float(product.price)
            quantity = int(cart_item.quantity)
            total_price += price * quantity
        except (ValueError, TypeError):
            pass
    
    total_fertilizer_price = 0
    
    for cart_fertilizer in cart_fertilizers:
        fertilizer = cart_fertilizer.fertilizer
        try:
            price = float(fertilizer.price)
            quantity = int(cart_fertilizer.quantity)
            total_fertilizer_price += price * quantity
        except (ValueError, TypeError):
            pass
    
    total_price += total_fertilizer_price

    total_medicine_price = 0
    
    for cart_medicine in cart_medicines:
        medicine = cart_medicine.medicine
        try:
            price = float(medicine.price)
            quantity = int(cart_medicine.quantity)
            total_medicine_price += price * quantity
        except (ValueError, TypeError):
            pass
    
    total_price += total_medicine_price
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'cart_fertilizers': cart_fertilizers,
        'cart_medicines': cart_medicines,
        'total_fertilizer_price': total_fertilizer_price,
        'total_medicine_price': total_medicine_price,

    }
    
    return render(request, 'web/cart.html', context)

def checkout(request):
    cart_items = CartItem.objects.select_related('product').all()
    cart_fertilizers = CartItem_Fertilizer.objects.select_related('fertilizer').all()  # Fetch all cart fertilizer items
    cart_medicines = CartItem_Medicine.objects.select_related('medicine').all()  # Fetch all cart fertilizer items


    total_price_items = sum(float(item.product.price) * item.quantity for item in cart_items)
    total_price_fertilizers = sum(float(item.fertilizer.price) * item.quantity for item in cart_fertilizers)
    total_price_medicines = sum(float(item.medicine.price) * item.quantity for item in cart_medicines)

    
    total_price = total_price_items + total_price_fertilizers + total_price_medicines
    
    context = {
        'cart_items': cart_items,
        'cart_fertilizers': cart_fertilizers,
        'cart_medicines': cart_medicines,
        'total_price': total_price,
    }
    
    return render(request, 'web/checkout.html', context)

