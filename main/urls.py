from django.contrib import admin
from django.urls import path
from .views import GradeViewSet

urlpatterns = [
    path('grades/', GradeViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    path('grades/<str:pk>', GradeViewSet.as_view({
        'get':'read',
        'put':'update',
        'delete':'delete',
    })),
]