import datetime

from django.db import models

# Create your models here.
import string
import random

from django.db import models
from django.utils.text import slugify

from api.models import User


class Category(models.Model):
    content = models.CharField(max_length=128)
    img = models.ImageField()
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.content}"

    class Meta:
        verbose_name = "Category"


class Subcategory(models.Model):
    name = models.CharField(max_length=128)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Character(models.Model):
    waranty = models.CharField(max_length=128)
    collection = models.CharField(max_length=128)
    matras = models.CharField(max_length=128)
    xususiyatlari = models.CharField(max_length=128)
    qoshimchalari = models.CharField(max_length=128)
    balandligi = models.CharField(max_length=128)
    mehanizm = models.CharField(max_length=128)
    massa = models.CharField(max_length=128)
    maqsad = models.CharField(max_length=128)
    razmer = models.CharField(max_length=128)
    qattiqlik = models.CharField(max_length=128)
    brand = models.CharField(max_length=128)

    class Meta:
        abstract = True


class Product(Character):
    sub_ctg = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=128)
    price = models.IntegerField()
    credit = models.IntegerField()
    bonus = models.IntegerField()
    size = models.CharField(max_length=122)

    def __str__(self):
        return f"{self.name}"


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    procent = models.IntegerField(blank=True, null=True, default=0)
    price = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.product.name}"

    # def __delete__(self, instance):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     print(">>>>", args)
    #     if args:
    #         pro = self.__class__.objects.get(pk=int(args[0])).end_date
    #         print(pro)
    #         if (pro.end_date - datetime.datetime.now()).total_seconds() < 0:
    #             pro.delete()

    def save(self, *args, **kwargs):
        self.procent = (self.price // self.product.price) * 100
        return super(Discount, self).save(*args, **kwargs)


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

    color = models.CharField(max_length=128)
    img = models.ImageField()

    def __str__(self):
        return f"{self.color}"


#  o'zgartirilgan joy


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    summa = models.IntegerField(blank=True, default=0)
    # img = models.ImageField()
    # serializer exclude ichida turadi, items ichiga tiqmisila
    updated_dt = models.DateTimeField(auto_now_add=False, auto_now=True)
    create_dt = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)

    def save(self, *args, **kwargs):
        self.summa = self.product.price * self.quantity
        return super(Basket, self).save(*args, **kwargs)


class Prosaved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    updated_dt = models.DateTimeField(auto_now_add=False, auto_now=True)
    create_dt = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)

    def __str__(self):
        return f"{self.product.name}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.text)[:30]


class Like(models.Model):
    commentary = models.ForeignKey(Comment, related_name="like", on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='requirement_comment_likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     if kwargs.get('key') == "like":
    #         self.dislike = False
    #     elif kwargs.get('key') == "dislike":
    #         self.like = False
    #     kwargs.pop('key')
    #     return super(Like, self).save(*args, **kwargs)
