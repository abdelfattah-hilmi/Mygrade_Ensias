from django.urls import path
from .views import GradeViewSet,MajorView,majorsListApiView

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
    path('majors/<str:id>',MajorView.as_view())
]