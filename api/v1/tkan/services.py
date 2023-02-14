from collections import OrderedDict
from sayt.models import Tkan
from base.sqlpaginator import SqlPaginator
from src.settings import PER_PAGE


def tkan_pag(requests):
    tkan = Tkan.objects.all()

    page = int(requests.GET.get('page', 1))
    limit = PER_PAGE
    offset = (page - 1) * limit
    print(tkan)
    result = []

    for i in range(offset, offset + limit):
        try:
            result.append(tkan_format(tkan[i]))
        except:
            break
    pagging = SqlPaginator(requests, page=page, per_page=limit, count=len(tkan))
    meta = pagging.get_paginated_response()

    return OrderedDict([
        ("items", result),
        ("meta", meta)
    ])


def get_one_tkan(data):
    return OrderedDict([
        ("item", tkan_format(data)),
    ])


def tkan_format(data):
    return OrderedDict([
        ('id', data.id),
        ('tkan_name', data.tkan_name),
        ("tkan_material", data.tkan_material),
        ('tkan_price', data.tkan_price)
    ])
