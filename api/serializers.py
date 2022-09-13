from rest_framework import serializers
from .models import HadishModel

class HadishSerializer(serializers.ModelSerializer):
    class Meta:
        model=HadishModel
        fields=['hadish_name','narated_by']