from rest_framework import serializers
from .models import Grades


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields='__all__'