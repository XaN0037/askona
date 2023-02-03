from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


class TkanImgInline(admin.StackedInline):
    model = TkanImg
    extra = 1


class ProductImgInline(admin.StackedInline):
    model = ProductImg
    extra = 1


class ColorImgInline(admin.StackedInline):
    model = ColorImg
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImgInline, ColorImgInline]


class TkanAdmin(admin.ModelAdmin):
    inlines = [TkanImgInline, ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tkan, TkanAdmin)
