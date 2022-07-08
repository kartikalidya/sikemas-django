from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from .models import*
from django.core import serializers
from .forms import FormOPD, Opd
from django.core import serializers
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text 
from django.core.mail import send_mail
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json
import time
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def penutup(request):
    return render(request,'Penutup.html')


def inputdata (request):
    if request.method== 'POST':
        email= request.POST.get('email')
        name =request.POST.get('name') 
        gender=request.POST.get('gender')
        age = request.POST.get("age")
        job = request.POST.get("job")
        last_education = request.POST.get("last_education")
        service_id = request.POST.get("service_id")
        x= People.objects.create(email=email, name=name, gender=gender, age=age, job=job, last_education=last_education, service_id=service_id)
        opds = Opd.objects.all()
        return render(request,"opd.html",{'opds':opds,'id': str(x.id)})
    else:
        return redirect('index')


    #password=staff.objects.filter(password=request.POST.get('password'))

def masuk(request):
    staff = Staff.objects.get(username=request.POST.get('username'), password=request.POST.get('password'))
    if staff :
        # request.session['staff'] = serializers.serialize('json', staff)\
        request.session['staff'] = staff.id
        return redirect('profile')
    else:
        return redirect('login')

def registrasi(request):
    return render(request,'registrasi.html')

def dataregistrasi (request):
    if request.method== 'POST':
        email= request.POST.get('email')
        mobile=request.POST.get ('mobile')
        name =request.POST.get('name')
        password=request.POST.get('password')
        Staff.objects.create(email=email, mobile=mobile, name=name, password=password)
        return redirect('profile')
    else:
        return redirect('registrasi')

def people(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = People.objects.all()

    return render(request, "people.html", context)

##CRUD OPD
#Create OPD
def add_opd(request):
    if request.method == "POST":
        form = FormOPD(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show-opd')
            except:
                pass
    else:
        form = FormOPD()
    return render(request, 'create-opd.html', {'form': form})

#Retrieve OPD
def show_opd(request):
    opds = Opd.objects.all()
    return render(request, "show_OPD.html", {'opds': opds})

#Update OPD
def edit_opd(request, opd_id):
    opd = Opd.objects.get(opd_id=opd_id)
    return render(request, 'update-opd.html', {'opd': opd})


def update_opd(request, opd_id):
    opd = Opd.objects.get(opd_id=opd_id)
    form = FormOPD(request.POST, instance=opd)
    if form.is_valid():
        form.save()
        return redirect("/show-opd")
    return render(request, 'update-opd.html', {'opd': opd})

#Delete OPD
def destroy_opd(request, opd_id):
    opd = Opd.objects.get(opd_id=opd_id)
    opd.delete()
    return redirect("/show-opd")

# SERVICE FOR ADMIN
# add service
def add_service(request, opd_id):
    opd = Opd.objects.get(opd_id=opd_id)
    if request.method == "GET":
        return render(request, "add_service.html", {'opd': opd})
    elif request.method == "POST":
        try:
            service_id = request.POST['service_id']
            service_name = request.POST['service_name']
            Service(service_id=service_id,
                    service_name=service_name, opd_id=opd_id).save()
            messages.success(request, 'Layanan berhasil ditambahkan!')
            opd = Opd.objects.get(opd_id=opd_id)
            return render(request, "add_service.html", {'opd': opd})
        except Exception as e:
            messages.success(request, 'Gagal menambahkan layanan!')
    return render(request, "add_service.html", {'opd': opd})

# delete service
def destroy_service(request, service_id):  
    service = Service.objects.get(service_id=service_id)  
    service.delete()
    return redirect("/show-opd")

# retrieve service for admin
def show_service(request, opd_id):  
    opd = Opd.objects.get(opd_id = opd_id)  
    return render(request,"lihat_layanan.html",{'opd':opd})

# SERVICE FOR PEOPLE
def service(request, opd_id, peopleid):
    if request.method == "GET":
        opd = Service.objects.all().filter(opd_id=opd_id)
        print(opd)
        return render(request,'layanan.html',{'opds':opd})
    elif request.method == "POST":
        print(request.POST['service_id'])
        responden = People.objects.get(id=int(peopleid))
        service = Service.objects.get(service_id = request.POST['service_id'])
        responden.service_id = service
        responden.save()
        return redirect('/kuesioner/'+ peopleid)


def send_action_email(user, request):
    current_site = get_current_site(request)
    email_subject= 'Set Password your Account'
    email_body= render_to_string('authentication/register.html',)
    {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk))
        
    }

def email(request):
    subject = 'Set Password your Account'
    message = ''
    email_from= settings.EMAIL_HOST_USER
    recipiet_list = ['nikorajagukguk647@gmail.com'] 
    send_mail(subject, message, email_from, recipient_list)
    return redirect('rederict to a new page')


def updateprofile (request):
    BASE_FILE = "sikemasapp/static/img/"
    id = request.session['staff']
    staff = Staff.objects.get(id=id)
    fs = FileSystemStorage()
    if request.method == 'POST' : 
        post  = request.POST
        if request.FILES.get('profile', False) :
            myfile = request.FILES['profile']
            extension = myfile.name.split(".")[1].lower()
            temp_name = str(int(time.time())) + "." + extension
            fs.save(BASE_FILE + temp_name, myfile)          
            if staff.profile != 'default_image.png':
                fs.delete(BASE_FILE + staff.profile)
            staff.profile = temp_name  

        staff.name = post.get("full_name")
        staff.email = post.get("email")
        staff.mobile = post.get("mobile")
        if post.get("password").strip() != "":
            staff.password = post.get("password")
        staff.save()
        return redirect('profile')
    return render(request, 'update_profile.html', {'staff':staff})

def profile (request):
    if request.session.has_key('staff'): 
        id = request.session['staff']
        staff = Staff.objects.get(id=id)
        return render(request,'profile.html', {
            'staff':staff
        })
    return redirect('login')

def Menu_CRUD_OPD(request):
    return render(request,'Menu_CRUD_OPD.html')

def kuesioner(request, peopleid):
    if request.method == 'GET':
        people = People.objects.get(id=int(peopleid))
        questions = SikemasappQuestionnaire.objects.all()
        return render(request, 'Kuesioner.html', {'people': people, 'questions': questions})
    elif request.method == 'POST':
        people = People.objects.get(id=int(peopleid))
        questions = SikemasappQuestionnaire.objects.all()
        for item in request.POST.keys():
            if item:
                if item[:2] == "K0":
                    Responden.objects.create(people=people, question=findbyid(
                        questions, item), answer=int(request.POST[item]))
        return redirect("/status-pengisian-kuesioner/")


def findbyid(arr, id) -> SikemasappQuestionnaire:
    for item in arr:
        if item.questionnaire_id == id:
            return item
    return None
