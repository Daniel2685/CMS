from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
import requests

from .models import MedicalHistory, EvolutionNote, Incapacity, Patient
from .forms import MedicalHistoryForm, EvolutionNoteForm, IncapacityForm, LoginForm, LaboratoryRequisitionForm, PrescriptionForm, PatientForm, RegisterPatientForm

def index(request):
    return HttpResponse('Bienvenido a la sección de doctores')

def register_patient(request):
    if request.method == 'POST':
        print("registro")
        register_patient_form = RegisterPatientForm(request.POST)
        if register_patient_form.is_valid():
            patient = register_patient_form.cleaned_data
            patient['dependency_id'] = int(patient['dependency_id'])
            print(patient)
            url_api = "https://api.ax01.dev/v1/patients"
            try:
                response = requests.post(url_api, json=patient)
                print("Status Code:", response.status_code)
                print("Response Text:", response.text)
                if response.status_code == 200:
                    return HttpResponse('Registro exitoso')
                else:
                    return HttpResponse('Registro fallido')
            except requests.RequestException as e:
                return HttpResponse('Error al enviar los datos')
    else:
        register_patient_form = RegisterPatientForm()
        return render(request, 'register_patient.html', {'register_patient_form' : register_patient_form})


def login(request):
    if request.method == 'POST':
        print('Iniciar sesión')
    else:
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form' : login_form})

def provide_consultation(request):
    medical_history_form = MedicalHistoryForm()
    evolution_note_form = EvolutionNoteForm()
    incapacity_form = IncapacityForm()
    laboratory_requisition_form = LaboratoryRequisitionForm()
    prescription_form = PrescriptionForm()
    doc_test = {
        'name' : 'name placeholder',
        'service' : 'service placeholder',
        'license1' : 'license placeholder',
        'license2' : 'license placeholder'
    }
    context = {
        'medical_history_form' : medical_history_form,
        'evolution_note_form' : evolution_note_form,
        'incapacity_form' : incapacity_form,
        'laboratory_requisition_form' : laboratory_requisition_form,
        'prescription_form' : prescription_form,
        'doctor' : doc_test
    }
    return render(request, 'consultation.html', context)

def process_medical_history(request):
    medical_history_form = MedicalHistoryForm(request.POST)
    if medical_history_form.is_valid():
        medical_history = medical_history_form.cleaned_data
        json_data = json.dumps(medical_history)
        print(json_data)
        return HttpResponse(json_data, content_type='application/json')
    else:
            # Retornar un error si el formulario no es válido
            return HttpResponse("Formulario no válido", status=400) 

def process_evolution_note(request):
    evolution_note_form = EvolutionNoteForm(request.POST)
    if evolution_note_form.is_valid():
        evolution_note = evolution_note_form.cleaned_data
        json_data = json.dumps(evolution_note)
        print(json_data)
        return HttpResponse(json_data, content_type='application/json')
    else:
            # Retornar un error si el formulario no es válido
            return HttpResponse("Formulario no válido", status=400)
        

def process_incapacity(request):
    incapacity_form = IncapacityForm(request.POST)
    if incapacity_form.is_valid():
        incapacity = incapacity_form.cleaned_data
        json_data = json.dumps(incapacity)
        print(json_data)

def process_laboratory_requisition(request):
    laboratory_requisition_form = LaboratoryRequisitionForm(request.POST)
    if laboratory_requisition_form.is_valid():
        laboratory_requisition = laboratory_requisition_form.cleaned_data
        json_data = json.dumps(laboratory_requisition)
        print(json_data)

def process_prescription(request):
    prescription_form = PrescriptionForm(request.POST)
    if prescription_form.is_valid():
        prescription = prescription_form.cleaned_data
        json_data = json.dumps(prescription)
        print(json_data)