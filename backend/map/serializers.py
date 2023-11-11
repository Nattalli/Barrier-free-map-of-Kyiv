from rest_framework import serializers
from .models import *


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class AdjacentStreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdjacentStreet
        fields = '__all__'


class SidewalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sidewalk
        fields = '__all__'


class SidewalkMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = SidewalkMap
        fields = '__all__'


class CommitIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitIssue
        fields = '__all__'


class SidewalkIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SidewalkIssue
        fields = '__all__'


class SidewalkIssueBorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SidewalkIssueBorder
        fields = '__all__'


class CrosswalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crosswalk
        fields = '__all__'


class CrosswalkIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrosswalkIssue
        fields = '__all__'


class CrosswalkBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrosswalkBenefit
        fields = '__all__'


class CrosswalkDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrosswalkDirection
        fields = '__all__'
