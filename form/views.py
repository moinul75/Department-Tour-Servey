from django.shortcuts import render
from django.http import JsonResponse
from .models import Student_Infos
import zipfile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os 
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request,'form.html')

excluded_fields = ['id']

#store all the pdf 
pdf_lists = []
#make a pdf 
def make_pdf(student_infos):
    #temp_directory 
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    temp_directory = os.path.join(BASE_DIR, 'pdf_file')
    
    pdf_filename = os.path.join(temp_directory, f"{student_infos.full_name}_{student_infos.id}.pdf")
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    y_position = 750
    line_spacing = 30

    c.setFont("Helvetica", 18)

    # Centering "Industrial Tour Info"
    text = "Industrial Tour Info"
    text_width = c.stringWidth(text, "Helvetica", 18)
    x_center = (letter[0] - text_width) / 2  # Calculate the center based on page width
    c.drawString(x_center, y_position, text)
    y_position -= line_spacing

    excluded_fields = ['id']  # Add fields to exclude here

    for field, value in student_infos.__dict__.items():
        if not field.startswith('_') and field not in excluded_fields:
            field_name = field.replace('_', ' ').capitalize()
            text = f"{field_name}: {value}"
            c.drawString(100, y_position, text)  # Adjust the x-coordinate to align to the left
            y_position -= line_spacing

    c.showPage()
    c.save()
    
    
#get all the files form pdf_file and then make zip 
def make_zip():
    #get  the directory 
    
    
    #read the file using file system 
    
    #make zip one to one coming from the loop 
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
        try:
            student_infos = Student_Infos(full_name=full_name,reg_no=reg_no,email=email,fathers_name=fathers_name,mothers_name=mothers_name,present_address=present_address,permanant_address=permanant_address,personal_contact_no=personal_contact_no,gurdians_contact_no=gurdian_contact_no,t_shirt_size=t_shirt_size,hobby=hobby,aim_in_life=aim_in_life)
            student_infos.save()
            #now make a pdf 
            make_pdf(student_infos)
            success = "Successfully Submit infos of " + full_name
            return JsonResponse({"success":success})
        except IntegrityError:
            error = "Email Must Be Uniques.."
            return JsonResponse({"error":error})
        
            
            
            
        
    
        
 
        

