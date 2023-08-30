from decimal import Decimal
from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField


class Banner(models.Model):
    # banner_image = models.ImageField(upload_to='banner')
    banner_video =models.FileField(upload_to='banner_video')
    banner_content = models.CharField(max_length=500)
    subhead = models.TextField()

    def __str__(self):
        return self.banner_content


class ProductCategory(models.Model):
    product_category = models.CharField(max_length=500)
    image = VersatileImageField(upload_to='product_category')
    description = models.TextField()
    order = models.PositiveIntegerField(null=True, unique=True)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.product_category
class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_image = VersatileImageField(upload_to='products')
    image1 = models.ImageField(upload_to='image1')
    image2 = models.ImageField(upload_to='image2')
    image3 = models.ImageField(upload_to='image3')
    product_type = models.CharField(max_length=300)
    product_name = models.CharField(max_length=300)
    price = models.IntegerField()
    details = models.TextField()
    description = HTMLField(null=True, blank=True)
    information = HTMLField(null=True, blank=True)
    planting_steps = HTMLField(null=True, blank=True)

    def __str__(self):
        return self.product_name


class Gallery(models.Model):
    gallery_image = VersatileImageField(upload_to='gallery')
    gallery_content = models.CharField(max_length=300)

    def __str__(self):
        return self.gallery_content


class Testimonial(models.Model):
    person_name = models.CharField(max_length=100)
    person_post = models.CharField(max_length=100)
    review = models.TextField()

    def __str__(self):
        return self.person_name


class Update(models.Model):
    update_image = VersatileImageField(upload_to='updates')
    day = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    update_head = models.CharField(max_length=500)
    update_details = models.TextField()
    description = HTMLField(null=True, blank=True)

    def __str__(self):
        return self.update_head


class Service(models.Model):
    service_image = VersatileImageField(upload_to='services')
    service_name = models.CharField(max_length=300)
    service_detail = models.TextField()

    def __str__(self):
        return self.service_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    message = models.TextField()


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Fertilizer(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fertilizer')
    inch=models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Medicine(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fertilizer')
    price = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Video(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    video_link = models.URLField(max_length=500)

    def __str__(self):
        return str(self.product_name)


class DetailProduct(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    inch = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return str(self.product_name)


class Catalogue(models.Model):
    catalogue = models.FileField(upload_to='catalogue')

    def __str__(self):
        return str(self.catalogue)

class CartItem(models.Model):
    product = models.ForeignKey(DetailProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total(self):
        return Decimal(self.product.price) * Decimal(self.quantity)

class Package(models.Model):
    name = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    inch = models.CharField(max_length=50)
    price = models.IntegerField()

class Quantity(models.Model):
    name = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    inch = models.CharField(max_length=50)
    price = models.IntegerField()

class CartItem_Fertilizer(models.Model):
    fertilizer = models.ForeignKey(Package, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total(self):
        return Decimal(self.fertilizer.price) * Decimal(self.quantity)
    
class CartItem_Medicine(models.Model):
    medicine = models.ForeignKey(Quantity, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total(self):
        return Decimal(self.medicine.price) * Decimal(self.quantity)