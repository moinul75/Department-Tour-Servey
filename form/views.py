from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_Infos

# Create your views here.
def home(request):
    return render(request,'form.html')


#make a pdf 
def make_pdf(request):
    pass 





#convert all pdf to zip 
def make_zip(request):
    pass 





#create form 
def create(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        reg_no = request.POST['reg_no']
        email = request.POST['email']
        fathers_name = request.POST['fathers_name']
        mothers_name = request.POST['mothers_name']
        present_address = request.POST['present_address']
        permanant_address = request.POST['permanant_address']
        personal_contact_no = request.POST['personal_contact_no']
        gurdian_contact_no = request.POST['gurdian_contact_no']
        t_shirt_size = request.POST['t_shirt_size']
        hobby = request.POST['hobby']
        aim_in_life = request.POST['aim_in_life']
        student_infos = Student_Infos(full_name=full_name,reg_no=reg_no,email=email,fathers_name=fathers_name,mothers_name=mothers_name,present_address=present_address,permanant_address=permanant_address,personal_contact_no=personal_contact_no,gurdians_contact_no=gurdian_contact_no,t_shirt_size=t_shirt_size,hobby=hobby,aim_in_life=aim_in_life)
        student_infos.save()
        print(student_infos)
 
        success = "Successfully Submit infos of " + full_name
        return HttpResponse(success)

