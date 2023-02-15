from rest_framework import serializers

from sayt.models import Tkan


class TkanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tkan
        fields = "__all__"

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.image = validated_data.get("image")

        instance.save()
        return instance

    def save(self, *args, **kwargs):
        print(args)
        print(kwargs)
        return super(TkanSerializer, self).save(*args, **kwargs)
