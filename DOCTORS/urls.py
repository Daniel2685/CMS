from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('provide_consultation', views.provide_consultation, name='provide_consultation'),
    path('login_doctor', views.login_doctor, name='login_doctor'),
    path('home_doctor', views.home_doctor, name='home_doctor'),
    path('process_medical_history', views.process_medical_history, name='process_medical_history'),
    path('process_evolution_note', views.process_evolution_note, name='process_evolution_note'),
    path('process_incapacity', views.process_incapacity, name='process_incapacity'),
    path('process_laboratory_requisition', views.process_laboratory_requisition, name='process_laboratory_requisition'),
    path('process_prescription', views.process_prescription, name='process_prescription'),
    path('register_patient', views.register_patient, name='register_patient'),
    path('register_doctor', views.register_doctor, name='register_doctor'),
    path('register_schedule', views.register_schedule, name='register_schedule'),
]