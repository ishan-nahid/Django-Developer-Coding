from django.db import models
from config.g_model import TimeStampMixin


# Create your models here.
class Variant(TimeStampMixin, models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True) 

    def __str__(self):
        return self.title
    # title = models.CharField(max_length=40, unique=True)
    # description = models.TextField()
    # active = models.BooleanField(default=True)


class Product(TimeStampMixin, models.Model):
    # title = models.CharField(max_length=255)
    # sku = models.SlugField(max_length=255, unique=True)
    # description = models.TextField()
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductImage(TimeStampMixin, models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    file_path = models.CharField(max_length=255)
    thumbnail = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # file_path = models.URLField()


class ProductVariant(TimeStampMixin, models.Model):
    id = models.BigAutoField(primary_key=True)
    variant = models.CharField(max_length=255)
    variant_id = models.BigIntegerField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='variants')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    variant_title = models.CharField(max_length=255)

    def __str__(self):
        return self.variant
    # variant_title = models.CharField(max_length=255)
    # variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductVariantPrice(TimeStampMixin, models.Model):
    id = models.BigAutoField(primary_key=True)
    product_variant_one = models.BigIntegerField()
    product_variant_two = models.BigIntegerField()
    product_variant_three = models.BigIntegerField()
    price = models.FloatField()
    stock = models.IntegerField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='variant_prices')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
    #                                         related_name='product_variant_one')
    # product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
    #                                         related_name='product_variant_two')
    # product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
    #                                           related_name='product_variant_three')
    # price = models.FloatField()
    # stock = models.FloatField()
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
