from collections import OrderedDict

from sayt.models import ProductImg, TkanImg, Subcategory, ColorImg, Discount, Character, Like
from src.settings import MEDIA_URL


def format(data):
    return OrderedDict([
        ('id', data.id),
        ('name', data.name),
        ('email', data.email),
        ('mobile', data.mobile),
    ])


def category_format(data):
    return OrderedDict([
        ('id', data.id),
        ('content', data.content),
        ('slug', data.slug),
        ('img', data.img.url),

    ])


def subcategory_format(data):
    return OrderedDict([
        ('id', data.id),
        ('name', data.name),
        ('ctg', None if not data.ctg else category_format(data.ctg)),
    ])


def tkan_format(data):
    return OrderedDict([
        ('id', data.id),
        ('product', product_format(data.product)),
        ('user_id', data.tkan_name),
        ('soni', data.tkan_material),
        ('summa', data.tkan_price),

    ])


def product_format(data):
    images = ProductImg.objects.select_related('product').filter(product_id=data.id).values('img')
    tkan = TkanImg.objects.select_related('product').filter(product_id=data.id).values('img')
    color = ColorImg.objects.select_related('product').filter(product=data)
    dis = Discount.objects.select_related('product').filter(product=data).first()
    # character = Character.objects.select_related('product').filter(product=data).first()
    if dis:
        dis = discount_format(dis)
    else:
        dis = {}
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
        ('waranty', data.waranty),
        ('collection', data.collection),
        ('matras', data.matras),
        ('xususiyatlari', data.xususiyatlari),
        ('qoshimchalari', data.qoshimchalari),
        ('balandligi', data.balandligi),
        ('mehanizm', data.mehanizm),
        ('massa', data.massa),
        ('maqsad', data.maqsad),
        ('razmer', data.razmer),
        ('qattiqlik', data.qattiqlik),
        ('brand', data.brand),


        ('images', [] if not images else [MEDIA_URL + x['img'] for x in images]),
        ('tkans', [] if not tkan else [MEDIA_URL + x['img'] for x in tkan]),
        ('color', colors),
        ('dis', dis)

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


def comment_format(data):
    return OrderedDict([
        ('comment_id', data.id),
        ('user', None if not data.user else format(data.user)),
        ('product', data.product.id),
        ('text', data.text),
        ('created_at', data.created_at),
        ('like', Like.objects.select_related('commentary', 'user').filter(commentary_id=data.id, like=True).count()),
        ('dislike', Like.objects.select_related('commentary', 'user').filter(commentary_id=data.id, dislike=True).count()),
    ])



def like_dislike_format(data):
    print('\n','bu like',data.like,'\n')
    return OrderedDict([



    ])


def discount_format(data):
    return OrderedDict([
        ('id', data.id),
        ('procent', data.procent),
        ('start_date', data.start_date),
        ('end_date', data.end_date),
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
