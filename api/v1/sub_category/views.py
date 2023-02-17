from rest_framework.generics import GenericAPIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from api.v1.auth.servise import BearerAuth
# from api.v1.comment.serializer import Commentserializer
from base.formats import category_format, subcategory_format, product_format
from sayt.models import Category, Subcategory, Product


class SubcategoryView(GenericAPIView):

    def get(self, requests, pk=None, *args, **kwargs):

        if pk:

            try:
                discount = Subcategory.objects.filter(pk=pk).first()
                if not discount:
                    return Response({"Error": "Sub category mavjud emas"})

                product = Product.objects.filter(sub_ctg=pk)
                resul = subcategory_format(discount)
                product_sub = [product_format(i) for i in product]
            except:
                resul = "Maxsulot topilmadi"
            return Response({"sub category": resul,
                             "Products subcategory:": product_sub
                             })

        result = [subcategory_format(i) for i in Subcategory.objects.all()]
