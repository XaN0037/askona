from rest_framework import serializers
from sayt.models import Basket


class Basketserializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'

