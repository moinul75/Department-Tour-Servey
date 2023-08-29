from django.shortcuts import render,HttpResponse
from django.http import JsonResponse, Http404
from .models import Student_Infos
import zipfile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os 
from django.db import IntegrityError
#for admin user 
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def home(request):
    return render(request,'form.html')



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

    excluded_fields = ['id','created_at','updated_at']  # Add fields to exclude here

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
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pdf_directory = os.path.join(BASE_DIR, 'pdf_file')
    
    zip_filename = os.path.join(BASE_DIR, 'pdf_files.zip')
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for pdf_filename in os.listdir(pdf_directory):
            if pdf_filename.endswith('.pdf'):
                pdf_path = os.path.join(pdf_directory, pdf_filename)
                zipf.write(pdf_path, os.path.basename(pdf_path))
                
                
#admin check 
def is_admin(user):
    return user.is_authenticated and user.is_superuser
        
#dwonload file 
@user_passes_test(is_admin)
def download_zip(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    zip_filename = os.path.join(BASE_DIR, 'pdf_files.zip')

    if os.path.exists(zip_filename):
        with open(zip_filename, 'rb') as zip_file:
            response = HttpResponse(zip_file.read(), content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename=pdf_files.zip'
            return response
    else:
        raise Http404("File not found")
    
    
    



    




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
        favourite_color = request.POST['favourite_color']
        t_shirt_size = request.POST['t_shirt_size']
        hobby = request.POST['hobby']
        aim_in_life = request.POST['aim_in_life']
        comment_type = request.POST.get('comment_type')
        comment = request.POST['comment']
        try:
            student_infos = Student_Infos(full_name=full_name, reg_no=reg_no, email=email, fathers_name=fathers_name, mothers_name=mothers_name, present_address=present_address, permanant_address=permanant_address, personal_contact_no=personal_contact_no, guardians_contact_no=gurdian_contact_no, favourite_color=favourite_color, t_shirt_size=t_shirt_size, hobby=hobby, aim_in_life=aim_in_life,comment_type=comment_type,comment=comment)
            student_infos.save()
            #now make a pdf 
            make_pdf(student_infos)
            success = "Successfully Submit infos of " + full_name
            #make all the file zipped 
            make_zip() 
            return JsonResponse({"success":success})
        except IntegrityError:
            error = "Email Must Be Uniques.."
            return JsonResponse({"error":error})
        
            
            
            
        
    
        
 
        

