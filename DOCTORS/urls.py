from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('home_superadmin', views.home_superadmin, name='home_superadmin'),
    path('home_admin', views.home_admin, name='home_admin'),
    path('home_doctor', views.home_doctor, name='home_doctor'),
    path('home_receptionist', views.home_receptionist, name='home_receptionist'),
    path('register_superadmin', views.register_superadmin, name='register_superadmin'),
    path('register_admin', views.register_admin, name='register_admin'),
    path('register_patient', views.register_patient, name='register_patient'),
    path('register_doctor', views.register_doctor, name='register_doctor'),
    path('register_receptionist', views.register_receptionist, name='register_receptionist'),
    path('register_specialty', views.register_specialty, name='register_specialty'),
    path('register_office', views.register_office, name='register_office'),
    path('register_schedule', views.register_schedule, name='register_schedule'),
    path('provide_consultation', views.provide_consultation, name='provide_consultation'),
    path('process_medical_history', views.process_medical_history, name='process_medical_history'),
    path('process_evolution_note', views.process_evolution_note, name='process_evolution_note'),
    path('process_incapacity', views.process_incapacity, name='process_incapacity'),
    path('process_laboratory_requisition', views.process_laboratory_requisition, name='process_laboratory_requisition'),
    path('process_prescription', views.process_prescription, name='process_prescription'),
]