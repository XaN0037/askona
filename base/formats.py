from collections import OrderedDict


def format(data):
    return OrderedDict([
        ('id', data.id),
        ('name', data.name),
        ('email', data.email),
        ('mobile', data.mobile),
    ])


def basket_format(data):
    return OrderedDict([
        ('id', data.id),
        ('product_id', data.product.id),
        ('user_id', data.user.id),
        ('soni', data.quantity),
        ('summa', data.summa),
        ('updated_dt', data.updated_dt),
        ('create_dt', data.create_dt),
    ])
