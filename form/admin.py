from django.contrib import admin
from .models import Student_Infos

# Register your models here.
admin.site.register(Student_Infos)

#change the site admin 
admin.site.site_title ='Industrial Tour Infos'
admin.site.site_header = 'Welcome to the website of industrial Tour infos'



