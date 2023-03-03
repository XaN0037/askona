from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.v1.auth.servise import BearerAuth
from api.v1.basket.serializer import Basketserializer
from base.formats import basket_format
from sayt.models import Product, Basket, ProductImg


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
        # img = ProductImg.objects.filter(product_id=product_id)
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

    def put(self, request, *args, **kwargs):

        bron_id = request.data['bron_id']
        quantity = request.data['quantity']
        if not bron_id:
            return Response({
                "Error": "bron_id kiritilmagan"
            })
        bron = Basket.objects.filter(pk=bron_id, user=request.user).first()

        if not bron:
            return Response({
                "Error": "bunaqa idli bron savatda mavjut emas"
            })

        if not quantity:
            return Response({
                "Error": "quantity kiritilmagan"
            })

        bron.quantity = quantity

        bron.save()
        return Response({
            "data": basket_format(bron)
        })

    def delete(self, request, *args, **kwargs):

        bron_id = request.data['bron_id']

        user = request.user
        if not bron_id:
            return Response({
                "Error": "bron_id kiritilmagan"
            })
        basket = Basket.objects.filter(pk=bron_id, user_id=user.id).first()

        if not basket:
            return Response({
                "Error": " bu id da bron topilmadi"
            })

        if basket:
            basket.delete()
            return Response({
                "Success": "Bron qilingan tarif o'chirib tashlandi"
            })


    def get(self, request, *args, **kwargs):
        user = request.user

        user_basket = Basket.objects.filter(user_id=request.user.id).first()
        if not user_basket:
            return Response({
                "Error": " bu user maxsulot bron qilmagan"
            })
        else:
            result = []
            for i in Basket.objects.all().filter(user_id=request.user.id):
                result.append(basket_format(i))

        result = {
            "summa": sum([x['summa'] for x in result]),
            "data": result
        }
        return Response(result)
