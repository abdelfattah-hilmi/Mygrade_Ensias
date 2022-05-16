from rest_framework import serializers
from .models import Grades,Majors,Subjects,Users



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','firstname','lastname','email','password','major']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

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