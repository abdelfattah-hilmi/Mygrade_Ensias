from rest_framework import serializers
from .models import Grades,Majors

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Majors
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = '__all__'