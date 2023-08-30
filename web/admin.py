from django.contrib import admin
from . models import Contact,Banner,Product,Gallery,Testimonial,Update,ProductCategory,Faq,Fertilizer,Medicine,Video,DetailProduct,Catalogue,CartItem,Package,Quantity,CartItem_Fertilizer,CartItem_Medicine

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','message')
admin.site.register(Contact,ContactAdmin)
admin.site.register(Banner)
# admin.site.register(Product)
admin.site.register(Gallery)
admin.site.register(Testimonial)
admin.site.register(Update)
admin.site.register(ProductCategory)
admin.site.register(Faq)
class PackageInline(admin.TabularInline):
    model = Package
    extra = 1  # Number of empty forms to display

class FertilizerAdmin(admin.ModelAdmin):
    inlines = [PackageInline]

admin.site.register(Fertilizer, FertilizerAdmin)
class QuantityInline(admin.TabularInline):
    model = Quantity
    extra = 1  # Number of empty forms to display

class MedicineAdmin(admin.ModelAdmin):
    inlines = [QuantityInline]

admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Video)
admin.site.register(Catalogue)
admin.site.register(CartItem)
class DetailProductInline(admin.TabularInline):
    model = DetailProduct
    extra = 1  # Number of empty forms to display

class ProductAdmin(admin.ModelAdmin):
    inlines = [DetailProductInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(DetailProduct) 

