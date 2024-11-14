from django.contrib.auth.models import BaseUserManager


#Custom user creation
class CustomUserManager(BaseUserManager):

    def create_user(self,name,email,password=None,**extra_field):
        
        if not email:
            raise ValueError("must use an email")
        
        email=self.normalize_email(email)
        user=self.model(email=email,name=name,**extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        # Call create_user instead of create_superuser
        return self.create_user(name="Superuser", email=email, password=password, **extra_fields)


    # def create_superuser(self,email,password=None,**extra_fields):

    #     extra_fields.setdefault('is_staff',True)
    #     extra_fields.setdefault('is_superuser',True)

    #     return self.create_superuser(email,password,**extra_fields)
