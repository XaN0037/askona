from rest_framework.generics import GenericAPIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from api.v1.auth.servise import BearerAuth
# from api.v1.comment.serializer import Commentserializer
from base.formats import category_format
from sayt.models import Category


class CategoryView(GenericAPIView):
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

        if method == "categoryadd":
            content = params['content']
            slug = params['slug']
            slug_try = Category.objects.filter(slug=slug).first()
            if slug_try:
                return Response({
                    "Error": " Bu slug bazada bor. Slug takrorlanmasligi shart."
                })

            root = Category()
            root.content = content
            root.slug = slug
            root.save()
            return Response({"Saved": category_format(root)})



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


    def delete(self,requeste,pk,*args, **kwargs):
        try:
            category = Category.objects.get(pk=pk).delete()
            result = f"categoriya {pk} id o'chirildi"
        except:
            result = f"{pk}da categoriya topilmadi"
        return Response(result)

