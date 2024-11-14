#from django
from django.contrib.auth import authenticate

#from rest framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

#from serializers
from .serializer import CustomUserSerializer

#from model
from .models import CustomUser

#registaring staff
class RegisterStaffView(APIView):

    def post(self,request):

        serializer=CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response(serializer.data)
            

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#staff login veiw
class LoginStaffView(generics.GenericAPIView):
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=CustomUserSerializer
    def post(self,request):
        user = CustomUser.objects.get(email=request.data['email'])

        if user is not None:
            #generating token for user
            refresh = RefreshToken.for_user(user)
            return Response({"msg":"succcessfully loged in","refresh":str(refresh),"access":str(refresh.access_token)},status=status.HTTP_201_CREATED)

        return Response({"msg":"username or password wrong"},status=status.HTTP_400_BAD_REQUEST)

#staff log out
class StaffLogoutView(APIView):
    def post(self,request):
        try:
            refresh_token= request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return  Response(status=status.HTTP_400_BAD_REQUEST)
        