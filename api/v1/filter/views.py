import json

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.db import connection
from contextlib import closing

from base.formats import product_format
from sayt.models import Product, ColorImg


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>', columns)
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class SearchView(GenericAPIView):

    def post(self, requests, cursor=None, *args, **kwargs):
        sql = f"""
            select * FROM sayt_product sp 
            WHERE lower  ("name") like lower ("%{requests.data['suz']}%")"""
        with closing(connection.cursor()) as cursor:
            cursor.execute(sql)
            print(cursor)
            data = dictfetchall(cursor)
        return Response(data)


# def checker(query_params):
#     '' if 'new' not in  query_params else query_params.pop('new')
#     '' if 'view' not in  query_params else query_params.pop('view')
#     return query_params
class Filteratsiya(GenericAPIView):
    def get(self, requests, *args, **kwargs):
        l = dict(requests.query_params)

        viewsql = ''
        order_by = '' if 'view' not in l and 'new' not in l else " order by "
        if "view" in l:
            viewsql += ' view desc '
        if 'new' in l:
            viewsql += ' pr.id desc '
        '' if 'new' not in l else l.pop('new')
        '' if 'view' not in l else l.pop('view')

        where = " where " if len(l) > 0 else ""

        if "ctg" in l:
            where += f" ctg.id = {l['ctg']} "
            if len(l) > 1:
                where += " and "

        if "color" in l:
            where += f""" c.color = '{l["color"]}' """

        sql = f"""
                select * from sayt_product pr
                inner join sayt_colorimg c on pr.id=c.product_id  
                INNER JOIN sayt_category ctg on pr.sub_ctg_id=ctg.id 
                
                {where}
                {order_by} {viewsql}
                """
        print(sql)
        respons = [product_format(x) for x in Product.objects.raw(sql)]

        return Response({
            "res": respons
        })
