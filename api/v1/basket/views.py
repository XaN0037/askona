from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.v1.auth.servise import BearerAuth
from api.v1.basket.serializer import Basketserializer
from base.formats import basket_format
from sayt.models import Product, Basket


class BasketView(GenericAPIView):
    serializer_class = Basketserializer
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

        basket = Basket.objects.filter(user_id=user.id).filter(product_id=product_id).first()
        if basket:
            basket.quantity += 1
            basket.summa = basket.quantity * product.price
            basket.save()

            return Response({'success': basket_format(basket)})

        root = Basket()
        root.user = user
        root.product = product
        root.summa = product.price
        root.save()

        return Response({'success': basket_format(root)})
