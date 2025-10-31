from django.shortcuts import render
from .models import Students
from .serializers import StudentsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class StudentsListCreateAPIView(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    
class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer