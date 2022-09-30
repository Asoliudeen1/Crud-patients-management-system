
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Patient
from django.contrib import messages



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

            return redirect('home') 
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
            return redirect('home')
    else:
        return render(request, 'app/add_patients.html')
