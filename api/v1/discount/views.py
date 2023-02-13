from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.v1.auth.servise import BearerAuth
from api.v1.discount.serializer import Discountserializer
from base.formats import comment_format, discount_format
from sayt.models import Comment, Product, Like, Discount


class DiscountView(GenericAPIView):
    serializer_class = Discountserializer

    def post(self, request, pk=None, *args, **kwargs):
        data = request.data
        print(">>>>>>>>>>>>>>>>>>>>>>>>>",data)

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
        root.procent = data["procent"]
        root.start_date = data["start_date"]
        root.end_date = data["end_date"]
        root.save()

        return Response({"saved":
            discount_format(root)
        })
        # get ga
        # discount.product_id = pk
        # discount.procent = data["procent"]
        # discount.start_date = data["start_date"]
        # discount.end_date = data["end_date"]
        # discount.save()
        # print('11111111111111111111111', discount)
        # return Response(
        #     discount_format(discount)
        # )




        #
        #
        # if not method:
        #     return Response({
        #         "Error": "method kiritilmagan"
        #     })
        #
        # if params is None:
        #     return Response({
        #         "Error": "params kiritilmagan"
        #     })
        #
        # if method == "commentadd":
        #     product_id = Product.objects.filter(pk=params["product_id"]).first()
        #     if not product_id:
        #         return Response({
        #             "Error": "bu id da product yo'q"
        #         })
        #
        #     root = Comment()
        #     root.user = user
        #     root.product = product_id
        #     root.text = params["text"]
        #     root.save()
        #     return Response({"saved": comment_format(root)})
        #
        # if method == "like":
        #     comment_id = Comment.objects.filter(pk=params["comment_id"]).first()
        #     if not comment_id:
        #         return Response({
        #             "Error": "bu id da comment yo'q"
        #         })
        #
        #     # if params['liketype'] == "like":
        #     #
        #     #     like = Like.objects.filter(commentary_id=comment_id, user_id=user.id).first()
        #     #
        #     #     if like:
        #     #         like.like = True
        #     #         like.save()
        #     #     else:
        #     #         root = Like()
        #     #         root.user = user
        #     #         root.like = True
        #     #         root.commentary = comment_id
        #     #         root.save()
        #     #     return Response({
        #     #         "succes": "liked"
        #     #     })
        #     #
        #     # if params['liketype'] == "dislike":
        #     #
        #     #     like = Like.objects.filter(commentary_id=comment_id, user_id=user.id).first()
        #     #
        #     #     if like:
        #     #         like.dislike = True
        #     #         like.save()
        #     #     else:
        #     #         root = Like()
        #     #         root.user = user
        #     #         root.dislike = True
        #     #         root.commentary = comment_id
        #     #         root.save()
        #     #     return Response({
        #     #         "succes": "disliked"
        #     #     })
        #     #
        #     like = Like.objects.get_or_create(commentary_id=comment_id, user_id=user.id)[0]
        #
        #     return Response(saver(like, params['liketype']))
