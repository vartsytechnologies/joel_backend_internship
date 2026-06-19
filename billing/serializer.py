from rest_framework import serializers
from .models import *

class AppliancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appliances
        fields = '__all__'