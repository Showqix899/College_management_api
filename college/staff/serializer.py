#from app
from .models import CustomUser

#from rest framework

from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:

        model=CustomUser
        fields=['name','email','password']
        extra_kwargs={'password':{'write_only':True}}


    def validate_email(self,email):

        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('email already exist!')
        return email
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
        