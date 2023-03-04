from rest_framework.generics import GenericAPIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from api.v1.auth.servise import BearerAuth
# from api.v1.comment.serializer import Commentserializer
from base.formats import category_format, subcategory_format
from sayt.models import Category, Subcategory


class SubcategoryView(GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (BearerAuth,)

    def post(self, request, *args, **kwargs):
        data = request.data
        method = data.get('method')
        params = data.get('params')
        if not method:
            return Response({
                "Error": "method kiritilmagan"
            })

        if params is None:
            return Response({
                "Error": "params kiritilmagan"
            })

        if method == "subcategoryadd":
            name = params['name']
            ctg = params['category']
            slug_try = Subcategory.objects.filter(name=name).first()
            if slug_try:
                return Response({
                    "Error": " Bu sub_category bazada bor. sub_category takrorlanmasligi shart."
                })

            root = Subcategory()
            root.name = name
            root.ctg = ctg
            root.save()
            return Response({"Saved": subcategory_format(root)})
        #
        # if method == "sub_delete":
        #     category_id = params['category_id']
        #     nott = Subcategory.objects.filter(pk=category_id).first()
        #     if not nott:
        #         return Response({
        #             "Error": " Bunaqa Id li category mavjud emas"
        #         })
        #     if nott:
        #         nott.delete()
        #         return Response({
        #             "succes": " Category o'chirildi"
        #         })

    def get(self, requests,pk=None, *args, **kwargs):

        if pk:

            try:
                discount = Category.objects.get(pk=pk)
                resul = category_format(discount)
            except:
                resul = "Maxsulot topilmadi"
            return Response({"data": resul})

        result = [category_format(i) for i in Category.objects.all()]
        if not result:
            result = "Category umuman yo'q"
        return Response({
            "data": result
        })




