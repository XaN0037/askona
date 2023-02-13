from rest_framework.generics import GenericAPIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from api.v1.auth.servise import BearerAuth
# from api.v1.comment.serializer import Commentserializer
from base.formats import category_format
from sayt.models import Category


class CategoryView(GenericAPIView):
    # serializer_class = Commentserializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (BearerAuth,)

    def post(self, request, *args, **kwargs):
        # user = request.user
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

        if method == "category_delete":
            category_id = params['category_id']
            nott = Category.objects.filter(pk=category_id).first()
            if not nott:
                return Response({
                    "Error": " Bunaqa Id li category mavjud emas"
                })
            if nott:
                nott.delete()
                return Response({
                    "succes": " Category o'chirildi"
                })


