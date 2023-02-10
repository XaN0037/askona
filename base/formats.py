from collections import OrderedDict

from sayt.models import ProductImg, TkanImg
from src.settings import MEDIA_URL


def format(data):
    return OrderedDict([
        ('id', data.id),
        ('name', data.name),
        ('email', data.email),
        ('mobile', data.mobile),
    ])


# def tkan_format(data):
#     return OrderedDict([
#         ('id', data.id),
#         ('product', product_format(data.product)),
#         ('user_id', data.tkan_name),
#         ('soni', data.tkan_material),
#         ('summa', data.tkan_price),
#
#     ])


def product_format(data):
    images = ProductImg.objects.select_related('product').filter(product_id=data.id).values('img')
    tkan = TkanImg.objects.select_related('product').filter(product_id=data.id).values('img')

    return OrderedDict([
        ('id', data.id),
        ('sub_ctg', data.sub_ctg.id),
        ('name', data.name),
        ('code', data.code),
        ('sale', data.sale),
        ('price', data.price),
        ('price', data.price),
        ('price_true', data.price_true),
        ('credit', data.credit),
        ('bonus', data.bonus),
        ('size', data.size),
        ('images', [] if not images else [MEDIA_URL + x['img'] for x in images]),
        ('tkans', [] if not tkan else [MEDIA_URL + x['img'] for x in tkan])


    ])


def character_format(data):
    return OrderedDict([
        ('id', data.waranty),
        ('collection', data.collection),
        ('matras', data.matras),
        ('xususiyatlari', data.xususiyatlari),
        ('qoshimchalari', data.qoshimchalari),
        ('balandligi', data.balandligi),
        ('mehanizm', data.mehanizm),
        ('maqsad', data.maqsad),
        ('razmer', data.razmer),
        ('qattiqlik', data.qattiqlik),
        ('brand', data.brand),

    ])


def basket_format(data):
    prod = product_format(data.product)
    return OrderedDict([
        ('id', data.id),
        ('product', prod),
        ('user_id', data.user.id),
        ('soni', data.quantity),
        ('summa', data.summa),
        ('updated_dt', data.updated_dt),
        ('create_dt', data.create_dt),
    ])


def prosaved_format(data):
    return OrderedDict([
        ('prosaved_id', data.id),
        ('product_id', data.product.id),
        ('user_id', data.user.id),
        ('updated_dt', data.updated_dt),
        ('create_dt', data.create_dt),
    ])


def colorimg_format(data):
    return OrderedDict([
        ('product', data.product),
        ('color', data.color),
        ('img', data.img.url),

    ])


def tkanImg_format(data):
    return OrderedDict([
        ('product', data.product),
        ('tkan', data.tkan),
        ('img', data.img.url),

    ])

# def format_course(data, lang=None):
#     images = CourseImage.objects.select_related('course').filter(course_id=data.id).values('image')
#
#     return OrderedDict([
#         ('id', data.id),
#         ('category', data.course_category),
#         ('image', data.image if not data.image else data.image.url),
#         ('video', data.video if not data.video else data.video.url),
#         ('title', data.title.get(lang) if lang else data.title),
#         ('years', data.years),
#         ('months', data.months),
#         ('about', data.about.get(lang) if lang else data.about),
#         ('images', [] if not images else [MEDIA_URL + x['image'] for x in images])
#     ])
