from django.contrib import admin

# Register your models here.
from .models import Product, Variant, ProductImage, ProductVariant, ProductVariantPrice

# Register your models here.
admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(ProductImage)
admin.site.register(ProductVariant)
admin.site.register(ProductVariantPrice)