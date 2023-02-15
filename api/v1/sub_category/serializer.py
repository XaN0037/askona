from rest_framework import serializers
from sayt.models import Subcategory


class Subcategoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'

