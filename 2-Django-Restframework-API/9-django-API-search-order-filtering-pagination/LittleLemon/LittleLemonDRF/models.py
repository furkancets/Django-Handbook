from django.db import models

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=225)
    
class MenuItem(models.Model):
    title = models.SlugField()
    price = models.DecimalField(decimal_places=2,max_digits=6)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
  
