from rest_framework import serializers
from .models import Grades,Majors,Subjects

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Majors
        fields = '__all__'

class SubjectSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = '__all__'