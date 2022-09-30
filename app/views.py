
import email
from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Patient
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator


@login_required(login_url='login')
def home(request):
    return render(request, 'app/home.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method =='POST':
        username = request.POST['username'].lower()
        password= request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            pass
            #messages.error(request, 'Username does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('patients') 
        else:
            pass
            #messages.error(request, 'Username or Password does not exist')
    return render(request, 'app/login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def addPatient(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') and (request.POST.get('description') or request.POST.get('description') is ''):
            patient = Patient()
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.description = request.POST.get('description')
            patient.save()
            messages.success(request, 'Patient added succesfully')
            return redirect('patients')
    else:
        return render(request, 'app/add_patients.html')


@login_required(login_url='login')
def Patients(request):
    if 'q' in request.GET:
        q = request.GET['q']
        patients = Patient.objects.filter(
            Q(name__icontains=q) | Q(phone=q) | Q(email=q) | Q(age=q) | Q(gender=q) | Q(description=q)
        ).order_by('-created_at')
    else:
        patients = Patient.objects.all().order_by('-created_at')

    paginator = Paginator(patients, 10)
    page = request.GET.get('page')
    patients = paginator.get_page(page)

    context = {
        'patients': patients,
    }
    return render(request, 'app/patients.html', context)

@login_required(login_url='login')
def deletePatient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    patient.delete()
    messages.success(request, "Patient deleted successfully!")
    return redirect('patients')
