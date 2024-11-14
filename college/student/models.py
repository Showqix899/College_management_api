from django.db import models

# Create your models here.
#data table for Department("Science","Arts","Commerce")
class Department(models.Model):
    dept_choice=[
                 ('S','Sceince'),
                 ('C','Comerce'),
                 ('A','Arts')
                 ]
    name=models.CharField(max_length=100,choices=dept_choice)


    def __str__(self):
        return self.name
    


        
        
    
#data table for student
class Student(models.Model):

    name=models.CharField(max_length=200)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    address=models.CharField(max_length=400)
    email=models.EmailField(max_length=200,null=True,blank=True)
    phone=models.CharField(max_length=11,unique=True)

    student_id=models.CharField(max_length=10,null=True,blank=True)
    section=models.CharField(max_length=30,null=True,blank=True)

    batch=models.IntegerField()
    enrolled_at=models.DateTimeField(auto_now_add=True)

    #overiding the save method for generate customized id
    def save(self,*args, **kwargs):
        if not self.student_id: #checking if the student id is provided

            id_initial = self.department.name[0]  # First letter of the department code (e.g., 'S' for Science)
            id_secodary=self.batch
            id_serial=Student.objects.all().count()+1
            self.student_id=f'{id_initial}{id_secodary}{id_serial}' #assigning the customized student id

        num_of_section=1 #initializing the num of section
        if Student.objects.filter(section=self.section,department=self.department ,batch=self.batch).count()>=30: #checking if a same department and same section has less then 30 students other wise
                                                                                                                  #increas the section number or open a new section to assign a student  
            num_of_section+=1

        self.section=self.department.name[0]+str(self.batch)+str(num_of_section) #assigning section
        return super().save(*args, **kwargs)
    

    def __str__(self):
        return self.name

