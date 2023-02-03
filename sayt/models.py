from django.db import models

# Create your models here.
import string
import random

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    content = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.content}"

    class Meta:
        verbose_name = "Category"


class Subcategory(models.Model):
    name = models.CharField(max_length=128)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)


class Character(models.Model):
    waranty = models.CharField(max_length=128)
    collection = models.CharField(max_length=128)
    matras = models.CharField(max_length=128)
    Xususiyatlari = models.CharField(max_length=128)
    qoshimchalari = models.CharField(max_length=128)
    balandligi = models.CharField(max_length=128)
    mehanizm = models.CharField(max_length=128)
    massa = models.CharField(max_length=128)
    Maqsad = models.CharField(max_length=128)
    razmer = models.CharField(max_length=128)
    qattiqlik = models.CharField(max_length=128)
    brand = models.CharField(max_length=128)

    class Meta:
        abstract = True


class Product(Character):
    sub_ctg = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=128)
    sale = models.DateTimeField()
    price = models.IntegerField()
    price_true = models.IntegerField(null=True, blank=True)
    credit = models.IntegerField()
    bonus = models.IntegerField()
    size = models.CharField(max_length=122)
    def __str__(self):
        return f"{self.name}"


class ProductImg(models.Model):
    img = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='images')


class Tkan(models.Model):
    tkan_name = models.CharField(max_length=128)
    tkan_material = models.CharField(max_length=126)
    tkan_price = models.IntegerField()

    def __str__(self):
        return f"{self.tkan_name}"


class TkanImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tkan = models.ForeignKey(Tkan, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="Tkan")

    def __str__(self):
        return f"{self.tkan}"


class ColorImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tkan = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(Tkan, max_length=128)
    img = models.ImageField()

    def __str__(self):
        return f"{self.color}"
