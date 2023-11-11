from rest_framework import serializers
from .models import MapPoint, Addition, MapPointCategory
import math


class SafeFloatField(serializers.FloatField):
    def to_representation(self, value):
        if math.isnan(value) or math.isinf(value):
            return 0.0
        return super().to_representation(value)


class AdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addition
        fields = ('title',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Addition
        fields = ('title',)


class MapPointSerializer(serializers.ModelSerializer):
    addition = AdditionSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    longitude = SafeFloatField()
    latitude = SafeFloatField()

    class Meta:
        model = MapPoint
        fields = ('title', 'comment', 'address', 'longitude', 'latitude', 'source', 'is_approved', 'addition', 'category', 'schedule')
