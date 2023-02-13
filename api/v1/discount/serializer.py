from rest_framework import serializers
from sayt.models import Comment, Discount


class Discountserializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

