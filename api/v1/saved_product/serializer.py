from rest_framework import serializers
from sayt.models import Prosaved


class Prosavedserializer(serializers.ModelSerializer):
    class Meta:
        model = Prosaved
        fields = '__all__'

