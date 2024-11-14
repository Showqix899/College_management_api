from django.db import models

# Create your models here.


#subject table
class Subject(models.Model):
    dept_choices=[
        ('S','Science'),
        ('C','Commerce'),
        ('A','Arts'),
    ]
    name=models.CharField(max_length=50)
    catagory=models.CharField(max_length=1,choices=dept_choices)
    subject_id=models.CharField(max_length=20,unique=True,blank=True)


    #customizing subject id
    def save(self,*args, **kwargs):
        if not self.subject_id:
           prefix=self.catagory
           word1=self.name[0].upper()
           word2=self.name[1].upper()
           count= Subject.objects.filter(name__startswith=self.name[:2],catagory=self.catagory).count()+1
           self.subject_id=f"{prefix}{word1}{word2}-{count}"
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
#teacher data table
class Teacher(models.Model):

    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    address=models.TextField(max_length=400)
    # subject=models.ManyToOneRel(Subject,on_delete=models.CASCADE)
    subject=models.ManyToManyField(Subject,related_name='teachers')

    def __str__(self):
        return self.name





