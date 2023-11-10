from rest_framework import serializers
from .models import MapPoint, Addition


class AdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addition
        fields = ('title',)


class MapPointSerializer(serializers.ModelSerializer):
    addition = AdditionSerializer(many=True, read_only=True)

    class Meta:
        model = MapPoint
        fields = ('title', 'comment', 'address', 'longitude', 'latitude', 'source', 'is_approved', 'addition')
