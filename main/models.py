from django.db import models

# Create your models here.
from django.db.models import UniqueConstraint


class Places(models.Model):
    id = models.TextField("Mall id", primary_key=True)
    addr_street = models.TextField("Mall Street Address", max_length=150)
    addr_housenumber = models.TextField("House number", max_length=20)
    building_levels = models.TextField("Building levels", default=1)
    name = models.TextField("Mall name", default="None")
    image_link = models.TextField("Mall image link", max_length=25555, unique=True)
    geometry = models.TextField("Geometry", default="None")

    def __str__(self):
        return self.name + ' ' + self.id

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"


class Nodes(models.Model):
    id = models.TextField("Node id", default="None", primary_key=True)
    name = models.TextField("Place name", default="None")
    geometry = models.TextField("Coordinates", default="None")

    def __str__(self):
        return self.name + ' ' + self.id

    class Meta:
        verbose_name = "Node"
        verbose_name_plural = "Nodes"


class Shop(models.Model):
    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"

    id = models.IntegerField('Shop id',default=1, primary_key=True)
    shop_name = models.CharField('Shop name', max_length=150)
    shop_link = models.TextField("Shop image link", max_length=25555, unique=True)
    mall_id = models.IntegerField("Mall id")

    def __str__(self):
        return self.shop_name

class Product(models.Model):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = 'main_product'

    id = models.IntegerField('Product id', default=1, primary_key=True)
    title = models.CharField('Product title', max_length=150)
    price = models.FloatField('Product price')
    category = models.CharField('Product category', max_length=100)
    description = models.TextField('Product description', max_length=2000, default="None")
    image_link = models.TextField("Product image link", max_length=25555, unique=True)
    shop_id = models.IntegerField("Shop id", default=1)

    def __str__(self):
        return self.title


