from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.v1.product.serializer import Productserializer
from api.v1.product.services import pro_format, pro_pag, get_one_pro
from base.formats import product_format
from sayt.models import Product


class ProductView(GenericAPIView):
    serializer_class = Productserializer

    def get_object(self, pk):
        try:
            root = Product.objects.get(pk=pk)
        except:
            raise NotFound(f'{pk}-chi iddagi malumot topilmadi')
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            result = get_one_pro(self.get_object(pk))
        else:
            result = pro_pag(requests)

        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(requests.data)

        return Response(pro_format(data))

    def put(self, requests, pk, *args, **kwargs):
        data = requests.data
        root = self.get_object(pk)
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        serializer.save()

        return Response(pro_format(root))

    def delete(self, requests, pk, *args, **kwargs):
        prod = Product.objects.filter(pk=pk).first()
        if prod:
            # prod.delete()
            result = "product o'chirildi"
        else:
            result = "product topilmadi"
        return Response({"reultat": result})
