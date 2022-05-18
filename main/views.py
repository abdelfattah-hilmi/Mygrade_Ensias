from rest_framework import viewsets,status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Users,Grades,Majors,Subjects
from .serializers import UsersSerializer,GradeSerializer,MajorSerializer,SubjectSerialzer
from rest_framework import generics # this is a good library to generate crud apis 


#TODO implement user authentication
# User registration ---------------

class RegisterUserView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

# login view -----------
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = Users.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        return Response({
            'succes':True
        })


# Major api_view : function based api-------------

@api_view(['GET','POST'])
def majorsListApiView(request):
    if request.method == 'GET':
        majors = Majors.objects.all()
        serializer = MajorSerializer(majors, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = MajorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MajorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Majors.objects.all()
    serializer_class = MajorSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

# Subject APIview-------------

class SubjectsListView(generics.ListCreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerialzer

class SubjectView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerialzer
    lookup_field = 'id'
    lookup_url_kwarg = 'id' 


# Grade APIView

class GradesListView(generics.ListCreateAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer

class GradeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradeSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'





"""

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

"""
    