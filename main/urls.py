from django.urls import path
from .views import GradesListView,GradeView,MajorView,SubjectsListView,SubjectView,majorsListApiView

#TODO implement regex urls


urlpatterns = [
    path('grades/', GradesListView.as_view()),
    path('grades/<str:pk>', GradeView.as_view()),
    path('majors/',majorsListApiView),
    path('majors/<str:id>',MajorView.as_view()),
    path('subjects/',SubjectsListView.as_view()),
    path('subjects/<str:id>',SubjectView.as_view()),
    
]