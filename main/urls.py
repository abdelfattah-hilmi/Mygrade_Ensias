from django.urls import path
from .views import GradeViewSet,MajorView,SubjectListView,SubjectView,majorsListApiView

#TODO implement regex urls


urlpatterns = [
    path('grades/', GradeViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    path('grades/<str:pk>', GradeViewSet.as_view({
        'get':'read',
        'put':'update',
        'delete':'destroy',
    })),
    path('majors/',majorsListApiView),
    path('majors/<str:id>',MajorView.as_view()),
    path('subjects/',SubjectListView.as_view()),
    path('subjects/<str:id>',SubjectView.as_view()),
    
]