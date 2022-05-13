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
        #/api/product/pk
        pass
    
    def update(self,request,pk=None):
        #/api/product/pk
        pass
    
    def destroy(self,request,pk=None):
        #/api/product/pk
        pass
    


