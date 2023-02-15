from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.v1.tkan.services import tkan_format, tkan_pag, get_one_tkan
from sayt.models import Tkan
from .serializer import TkanSerializer


class PartnersView(GenericAPIView):
    serializer_class = TkanSerializer

    def get_object(self, pk):
        try:
            root = Tkan.objects.get(pk=pk)
        except:
            raise NotFound(f'{pk}-chi iddagi malumot topilmadi')
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            result = get_one_tkan(self.get_object(pk))
        else:
            result = tkan_pag(requests)

        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(requests.data)

        return Response(tkan_format(data))

    def put(self, requests, pk, *args, **kwargs):
        root = self.get_object(pk)
        data = requests.data
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)

        return Response(tkan_format(data))

    def delete(self, requests, pk, *args, **kwargs):
        root = Tkan.objects.get(pk=pk)
        root.delete()
        return Response({"Success": "Tkan malumotlari muoffaqiyatli o'chirildi"})