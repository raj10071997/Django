from .models import AppDhanraj
from rest_framework import serializers

class Serializer(serializers.ModelSerializer):

    class Meta:
        model = AppDhanraj
        fields = '__all__'
