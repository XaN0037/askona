from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.v1.auth.servise import BearerAuth
from api.v1.comment.serializer import Commentserializer
from base.formats import comment_format, like_dislike_format
from sayt.models import Comment, Product, Like


def saver(model, type, comment):
    model.dislike = True if type == "dislike" else False
    model.like = True if type == "like" else False
    model.save()


def dl(self, cmt):
    return {
        "like": self.objects.filter(commentary=cmt, like=True).count(),
        "dislike": self.objects.filter(commentary=cmt, dislike=True).count()
    }


class CommentView(GenericAPIView):
    serializer_class = Commentserializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerAuth,)

    def post(self, request, *args, **kwargs):

        user = request.user
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

        if method == "commentadd":
            product_id = Product.objects.filter(pk=params["product_id"]).first()
            if not product_id:
                return Response({
                    "Error": "bu id da product yo'q"
                })

            root = Comment()
            root.user = user
            root.product = product_id
            root.text = params["text"]
            root.save()
            return Response({"saved": comment_format(root)})

        if method == "like":
            comment_id = Comment.objects.filter(pk=params["comment_id"]).first()
            if not comment_id:
                return Response({
                    "Error": "bu id da comment yo'q"
                })

            # if params['liketype'] == "like":
            #
            #     like = Like.objects.filter(commentary_id=comment_id, user_id=user.id).first()
            #
            #     if like:
            #         like.like = True
            #         like.save()
            #     else:
            #         root = Like()
            #         root.user = user
            #         root.like = True
            #         root.commentary = comment_id
            #         root.save()
            #     return Response({
            #         "succes": "liked"
            #     })
            #
            # if params['liketype'] == "dislike":
            #
            #     like = Like.objects.filter(commentary_id=comment_id, user_id=user.id).first()
            #
            #     if like:
            #         like.dislike = True
            #         like.save()
            #     else:
            #         root = Like()
            #         root.user = user
            #         root.dislike = True
            #         root.commentary = comment_id
            #         root.save()
            #     return Response({
            #         "succes": "disliked"
            #     })
            #
            like = Like.objects.get_or_create(commentary_id=params["comment_id"], user_id=user.id)[0]
            saver(like, params['liketype'], comment=comment_id)
            return Response(dl(Like, comment_id))


class Comments(GenericAPIView):
    def get(self, requests, pk, *args, **kwargs):
        if not pk:
            return Response({
                "Error": "pk kiritilmagan"
            })

        comments = Comment.objects.filter(product_id=pk)
        result = [comment_format(x) for x in comments]
        print(">>>>>>>>>>>>>",result)
        return Response({
            # "count":dl(Like,comments.id),
            "cnt": len(result),
            "data": result
        })
