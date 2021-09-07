from rest_framework import serializers
from .models import *


# serializer used to store and show the data
class CatDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CatDetailModel
        fields = '__all__'

    def validate(self, attrs):
        name = attrs.get('name', '')

        if CatDetailModel.objects.filter(name=name).exists():
            raise serializers.ValidationError({'name': "name already exists"})

        return super().validate(attrs)