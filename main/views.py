from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Grades
from .serializers import GradeSerializer

class GradeViewSet(viewsets.ViewSet):
    def list(self,request):
        grades = Grades.objects.all()
        serializer = GradeSerializer(grades,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer= GradeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def read(self,request,pk=None):
        grade = Grades.objects.get(id=pk)
        serializer = GradeSerializer(grade)
        return Response(serializer.data)
    
    def update(self,request,pk=None):
        grade = Grades.objects.get(id=pk)
        serializer = GradeSerializer(instance=grade, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    
    def destroy(self,request,pk=None):
        grade = Grades.objects.get(id=pk)
        grade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    