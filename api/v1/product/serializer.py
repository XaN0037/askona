from rest_framework import serializers
from sayt.models import  Product


class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

