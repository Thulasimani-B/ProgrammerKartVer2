from django.contrib import admin

# importing all models
from . models import Product,Customer

admin.site.register(Product)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','state','zipcode']