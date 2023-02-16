from collections import OrderedDict

from django.conf.global_settings import MEDIA_URL

from base.formats import subcategory_format, discount_format
from sayt.models import Product, ProductImg, TkanImg, ColorImg, Discount
from base.sqlpaginator import SqlPaginator
from src.settings import PER_PAGE


def pro_pag(requests):
    tkan = Product.objects.all()

    page = int(requests.GET.get('page', 1))
    limit = PER_PAGE
    offset = (page - 1) * limit
    print(tkan)
    result = []

    for i in range(offset, offset + limit):
        try:
            result.append(pro_format(tkan[i]))
        except:
            break
    pagging = SqlPaginator(requests, page=page, per_page=limit, count=len(tkan))
    meta = pagging.get_paginated_response()

    return OrderedDict([
        ("items", result),
        ("meta", meta)
    ])


def get_one_pro(data):
    return OrderedDict([
        ("item", pro_format(data)),
    ])


def pro_format(data):
    images = ProductImg.objects.select_related('product').filter(product_id=data.id).values('img')
    tkan = TkanImg.objects.select_related('product').filter(product_id=data.id).values('img')
    color = ColorImg.objects.select_related('product').filter(product=data)
    dis = Discount.objects.select_related('product').filter(product=data).first()
    if dis:
        dis = discount_format(dis)
    else:
        dis = {}
    print(color)
    colors = []
    for i in color:
        colors.append({
            "imgs": "" if not i.img else i.img.url,
            "name": i.color
        })

    return OrderedDict([
        ('id', data.id),
        ('sub_ctg', None if not data.sub_ctg else subcategory_format(data.sub_ctg)),
        ('name', data.name),
        ('code', data.code),
        ('price', data.price),
        ('credit', data.credit),
        ('bonus', data.bonus),
        ('size', data.size),
        ('images', [] if not images else [MEDIA_URL + x['img'] for x in images]),
        ('tkans', [] if not tkan else [MEDIA_URL + x['img'] for x in tkan]),
        ('color', colors),
        ('dis', dis)
    ])
