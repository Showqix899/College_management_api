from rest_framework import serializers

from .models import Student,Department

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields=['id','name','phone','department','address','email','student_id','section','batch']
        read_only_field=['student_id']

