from rest_framework import serializers

from .models import EducationModules


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationModules
        fields = ['number', 'name', 'description']
