from rest_framework import serializers
from sayt.models import  Product


class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        if res.get('sub_ctg'):
            res['sub_ctg'] = {
                'id': instance.sub_ctg.id,
                'name': instance.sub_ctg.name,
            }
        return res



