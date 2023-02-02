from collections import OrderedDict


def format(data):
    return OrderedDict([
        ('id', data.id),
        ('name', data.name),
        ('email', data.email),
        ('mobile', data.mobile),
    ])