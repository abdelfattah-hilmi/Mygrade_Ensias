from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Grades,Majors
from .serializers import GradeSerializer,MajorSerializer



@api_view(['GET','POST'])
def majorApiView(request):
    if request.method == 'GET':
        majors = Majors.objects.all()
        serializer = MajorSerializer(majors, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = MajorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




# Grade view  
class GradeViewSet(viewsets.ViewSet):
    def list(self,request):
        grades = Grades.objects.all()
        serializer = GradeSerializer(grades,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = GradeSerializer(data = request.data)
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
    