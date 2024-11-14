from rest_framework import serializers

from .models import Subject,Teacher

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model=Subject
        fields=['name','catagory','subject_id','teachers']
        read_only_fields=['subject_id']


        
class TeacherSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'address', 'subject']
        

    def create(self, validated_data):
        # Extract subject data from validated data
        subjects_data = validated_data.pop('subject')

        # Create the Teacher instance
        teacher_instance = Teacher.objects.create(**validated_data)

        # Iterate over each subject data
        for subject_data in subjects_data:
            # Check if the subject already exists
            subject_instance, created = Subject.objects.get_or_create(
                name=subject_data['name'],
                catagory=subject_data['catagory']
            )
            # Associate the subject with the teacher
            teacher_instance.subject.add(subject_instance)

        return teacher_instance