from django.urls import path
from .views import StudentsListCreateAPIView, StudentDetailAPIView

urlpatterns = [
    path('student/', StudentsListCreateAPIView.as_view(), name='student-list'),
    path('student/<int:pk>/', StudentDetailAPIView.as_view(), name='student-details'),
]