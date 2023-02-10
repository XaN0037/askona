from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.v1.auth.servise import BearerAuth
from api.v1.saved_product.serializer import Prosavedserializer
from base.formats import prosaved_format
from sayt.models import Product, Prosaved


class ProsavedView(GenericAPIView):
    serializer_class = Prosavedserializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerAuth,)

    def post(self, request, *args, **kwargs):
        product_id = request.data['product_id']
        user = request.user
        if not product_id:
            return Response({
                "Error": "product_id kiritilmagan"
            })

        product = Product.objects.filter(pk=product_id).first()

        if not product:
            return Response({
                "Error": "bunaqa idli product mavjut emas"
            })

        product_saved = Prosaved.objects.filter(product_id=product_id).first()

        if product_saved:
            return Response({
                "Error": "bunaqa id_li product allaqachon saqlangan"
            })
        
        root = Prosaved()
        root.user = user
        root.product_id = product_id
        root.save()

        return Response({'success': prosaved_format(root)})

    def delete(self, request, *args, **kwargs):
        data = request.data
        if not data:
            return Response({
                "Error": "saved_id kiritilmagan"
            })

        saved_id = data['saved_id']

        product_saved_id = Prosaved.objects.filter(pk=saved_id).first()

        if not product_saved_id:
            return Response({
                "Error": "bunaqa id li product saqlanmagan"
            })
        if product_saved_id:
            product_saved_id.delete()
            return Response({
                "Success": "saqlangan product o'chirib tashlandi"
            })


