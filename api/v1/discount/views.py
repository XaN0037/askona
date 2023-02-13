from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from api.v1.discount.serializer import Discountserializer
from base.formats import discount_format
from sayt.models import Product, Discount


class DiscountView(GenericAPIView):
    serializer_class = Discountserializer

    def post(self, request, pk=None, *args, **kwargs):
        data = request.data

        product = Product.objects.filter(pk=pk).first()
        if not product:
            return Response({
                "Error": "Bunday product mavjud emas"
            })

        discount = Discount.objects.filter(product_id=pk).first()

        if discount:
            return Response({
                "Error": "Bunday product bazada bor"
            })

        root = Discount()
        root.product_id = pk
        root.price = data["price"]
        root.start_date = data["start_date"]
        root.end_date = data["end_date"]
        root.save()

        return Response({
            "data": discount_format(root)
        })

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            #     discount = Discount.objects.filter(pk=pk).first()
            #     if discount:
            #         return Response({
            #             "data": discount_format(discount)
            #         })
            #
            #     return Response({
            #         "Maxsulot topilmadi"
            #     })
            #
            # result = [discount_format(i) for i in Discount.objects.all()]
            # return Response({
            #     "data": result
            #     })
            try:
                discount = Discount.objects.get(pk=pk)
                resul = discount_format(discount)
            except:
                resul = "Maxsulot topilmadi"
            return Response({"data": resul})

        result = [discount_format(i) for i in Discount.objects.all()]
        return Response({
            "data": result
        })

    def delete(self, request, pk, *args, **kwargs):
        try:
            discount = Discount.objects.get(pk=pk).delete()
            res = f"{discount} o'chirib yuborildi"
        except:
            res = "Bunday product discountda yo'q"
        return Response({
            "result": res
        })
