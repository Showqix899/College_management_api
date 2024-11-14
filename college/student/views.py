from django.shortcuts import render
from rest_framework import permissions


from rest_framework.viewsets import ModelViewSet


from .serializers import StudentSerializer

from .models import Student

# Create your views here.


#student create,update,delete,detail view
class studentView(ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

