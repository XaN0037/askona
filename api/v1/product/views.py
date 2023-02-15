from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.v1.product.serializer import Productserializer
from base.formats import product_format
from sayt.models import Product


class ProductView(GenericAPIView):
    serializer_class = Productserializer

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            try:
                result = product_format(Product.objects.get(pk=pk))
                # print(result)
                # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', result)
                return Response(result)
            except:

                result = {"ERROR": f"{pk} id bo'yicha hech qanday ma'lumot topilmadi"}
                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', result)
                return Response(result)

        else:
            result = []
            for i in Product.objects.all():
                result.append(product_format(i))

        return Response(result)



    def put(self, requests, pk, *args, **kwargs):

        data = requests.data
        new = Product.objects.get(pk=pk)
        serializer = self.get_serializer(data=data, instance=new, partial=True)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()
        return Response(product_format(root))