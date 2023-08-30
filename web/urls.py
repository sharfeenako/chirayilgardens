from . import views
from django.urls import path


app_name='web'

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('shop',views.shop,name='shop'),
    path('shop_single/<int:id>/',views.shop_single,name='shop_single'),
    path('shop_detail/<int:id>/',views.shop_detail,name='shop_detail'),
    path('gallery',views.gallery,name='gallery'),
    path('fertilizer_medicine',views.substance,name='substance'),
    path('fertilizer_detail/<int:id>',views.fertilizer_detail,name='fertilizer_detail'),
    path('medicine_detail/<int:id>',views.medicine_detail,name='medicine_detail'),
    path('guide',views.guide,name='guide'),
    path('updates',views.updates,name='updates'),
    path('update_detail/<int:id>/',views.update_detail,name='update_detail'),
    path('contact',views.contact,name='contact'),
    # path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/', views.cart, name='cart'),
    path('cart/add/<int:id>/', views.cart_add, name='add_to_cart'),
    path('cart/fertilizer/<int:id>/', views.cart_fertlizer, name='fertilizer_cart'),
     path('cart/medicine/<int:id>/', views.cart_medicine, name='medicine_cart'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/',views.cart,name='cart'),
    path('checkout/', views.checkout, name='checkout'),

]
    
