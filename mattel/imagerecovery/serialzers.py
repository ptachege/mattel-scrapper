from rest_framework import serializers
from .models import *


class TireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tire
        fields = '__all__'


class LegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogoToys
        fields = '__all__'
