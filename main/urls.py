from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import LoginView,RegisterUserView,GradesListView,GradeView,MajorView,SubjectsListView,SubjectView,MajorsListView

#TODO implement regex urls


urlpatterns = [
    path('login/',LoginView.as_view()),
    path('register/',RegisterUserView.as_view()),
    path('grades/', GradesListView.as_view()),
    path('grades/<str:pk>', GradeView.as_view()),
    path('majors/',MajorsListView.as_view()),
    path('majors/<str:id>',MajorView.as_view()),
    path('subjects/',SubjectsListView.as_view()),
    path('subjects/<str:id>',SubjectView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]