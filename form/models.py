from django.db import models

# Create your models here.
#fields are now full_name,reg_no,fathers_name,mothers_name,present_address,permanant_address,personal_contact_no,gurdian_contact_no,t-shirt_size,hobby,aim_in_life
class Student_Infos(models.Model):
    COMMENT_CHOICES = [
        ('advice', 'Advice'),
        ('complain', 'Complain'),
    ]
    
    full_name = models.CharField(max_length=255)
    reg_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=200, unique=True, error_messages={
        'unique': "This email address is already in use."
    })
    fathers_name = models.CharField(max_length=200)
    mothers_name = models.CharField(max_length=200)
    present_address = models.CharField(max_length=200)
    permanant_address = models.CharField(max_length=200)
    personal_contact_no = models.CharField(max_length=15)
    guardians_contact_no = models.CharField(max_length=15)
    favourite_color = models.CharField(max_length=20)
    t_shirt_size = models.CharField(max_length=15)
    hobby = models.CharField(max_length=200)
    aim_in_life = models.CharField(max_length=200)
    comment_type = models.CharField(max_length=10, choices=COMMENT_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Student Info"
    
    def __str__(self):
        return self.full_name

    
    
    
    
