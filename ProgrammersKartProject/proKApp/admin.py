from django.contrib import admin

# importing all models
from . models import Product,Customer,Cart



@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','description','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','state','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']