from rest_framework import viewsets
from rest_framework.response import Response
from .models import Grades
from .serializers import GradeSerializer

class GradeViewSet(viewsets.ViewSet):
    def list(self,request):
        grades = Grades.objects.all()
        serializer = GradeSerializer(grades,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        #/api/product
        pass
    
    def read(self,request,pk=None):
        #/api/product/pk
        pass
    
    def update(self,request,pk=None):
        #/api/product/pk
        pass
    
    def destroy(self,request,pk=None):
        #/api/product/pk
        pass
    


