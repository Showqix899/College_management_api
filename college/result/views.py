
#from django
from django.shortcuts import render
from django.shortcuts import get_object_or_404


#from rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

#from models 
from .models import StudentResult

#from student apps
from student.models import Student
from student.serializers import StudentSerializer



#from student serializer
from .serializers import StudentResultSerializer
# Create your views here.


#for get student result and post result
class StudentResultView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        results=StudentResult.objects.all();

        serializer=StudentResultSerializer(results,many=True)

        return Response(serializer.data,status=status.HTTP_201_CREATED)
    

    def post(self,request):

        result=request.data
        serializer=StudentResultSerializer(data=result)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        


#to update result and  delete
class StudentResultUpdatedeleteView(APIView):
    #for jwt authentication validation
    permission_classes=[permissions.IsAuthenticated]
    def put(self,request,pk):
        result=get_object_or_404(StudentResult,pk=pk) #extract the student result instance to update 
        serializer=StudentResultSerializer(result,data=request.data)

        if serializer.is_valid(): #checking for validation
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        
        return Response({"msg":"something went wrong"},status=status.HTTP_400_BAD_REQUEST)
    
    #to delete result data
    def delete(self,request,pk):
        result=get_object_or_404(StudentResult,pk=pk)
        result.delete()
        return Response({'msg':'publisher deleted'})
    
#for a student result detail
class StudentResultDetail(APIView):
    #jwt validation
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,id):
        student_detail=get_object_or_404(Student,student_id=id) #extract student detail from Student Table as per Student ID
        result_detail=get_object_or_404(StudentResult,student_id=id) #extract result detali of a Student from 

        result_serializer=StudentResultSerializer(result_detail) #serializing the data
        student_serializer=StudentSerializer(student_detail) #serializing the data

        return Response({"result_detail":result_serializer.data,"student_serializer":student_serializer.data},status=status.HTTP_205_RESET_CONTENT)
        