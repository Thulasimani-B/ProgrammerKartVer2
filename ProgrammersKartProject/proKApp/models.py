from django.db import models

# Create your models here.

# class Products(models.Model):
#     prd_name = models.CharField(max_length=30,primary_key=True)

CATEGORY_CHOICES = (
    ('OR','Ornamental'),
    ('FR','Furniture'),
    ('AR','Accessories'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    description = models.TextField()
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title