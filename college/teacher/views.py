from django.shortcuts import render


#rest framework
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions


##from app .models
from .models import Teacher,Subject

##from app .serializer
from .serializers import TeacherSerializer,SubjectSerializer

# Create your views here.

#Teacher create,update,delete,detail view
class TeacherView(ModelViewSet):
    #jwt validation
    permission_classes=[permissions.IsAuthenticated]
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer

#subject create,update,delete,detail view
class SubjectView(ModelViewSet):
    #jwt validation
    permission_classes=[permissions.IsAuthenticated]
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer



