from . import views
from django.urls import path
    
urlpatterns = [
        path('', views.home, name='home'),
        
        #login Path
        path('loginpage/', views.loginPage, name='login'),
        #logout Path
        path('logout/', views.logoutpage, name='logout'),

        #CRUD
        path('patients/', views.Patients, name='patients'),
        path('add_patient/', views.addPatient, name='add-patient'),
        
]