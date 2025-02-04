import datetime
from datetime import timedelta, datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
import requests

from .models import MedicalHistory, EvolutionNote, Incapacity, Patient
from .forms import (MedicalHistoryForm, RegisterScheduleForm, EvolutionNoteForm, IncapacityForm, DoctorLoginForm, LaboratoryRequisitionForm, PrescriptionForm, 
RegisterPatientForm, RegisterDoctorForm, RegisterSuperadminForm, RegisterAdminForm, RegisterReceptionistForm, RegisterSpecialtyForm, RegisterOfficeForm,LoginForm
)

def index(request):
    return HttpResponse('Bienvenido a la sección de doctores')

def register_superadmin(request):
    user_data_cookie = request.COOKIES.get('userData')
    if user_data_cookie:
        user_data = json.loads(user_data_cookie)
        role = int(user_data.get('role'))
        if role == 1:
            DEPENDENCIES = [
                (1, "SUTESUAEM"),
                (2, "FAAPA"),
                (3, "ALUMNO"),
                (4, "CONFIANZA"),
                (5, "EXTERNO")
            ] 
            if request.method == 'POST':
                form = RegisterSuperadminForm(request.POST)
                form.fields['dependency_id'].choices = DEPENDENCIES
                if form.is_valid():
                    superadmin = form.cleaned_data
                    superadmin.pop('password2', None)
                    superadmin['dependency_id'] = int(superadmin['dependency_id'])
                    auth_token = user_data.get('token')
                    headers = {
                        'Authorization': f'Bearer {auth_token}',
                        'Content-Type': 'application/json'
                    }
                    url_api = "https://api.ax01.dev/v1/admin/superadmin"
                    try:
                        response = requests.post(url_api, json=superadmin, headers=headers)
                        print("Status Code:", response.status_code)
                        if response.status_code == 200:
                            return HttpResponse('Registro exitoso')
                        else:
                            return HttpResponse('Registro fallido')
                    except requests.RequestException as e:
                        return HttpResponse('Error al enviar los datos')
                else:
                    return render(request, 'register_superadmin.html', {'register_superadmin_form': form})
            else:
                form = RegisterSuperadminForm()
                form.fields['dependency_id'].choices = DEPENDENCIES
                return render(request, 'register_superadmin.html', {'register_superadmin_form': form})
        else:
            return HttpResponse('Permiso denegado')
    else:
        return HttpResponse('Permiso denegado')


def register_admin(request):
    user_data_cookie = request.COOKIES.get('userData')
    if(user_data_cookie):
        user_data = json.loads(user_data_cookie)
        role = int(user_data.get('role'))
        if(role == 1 or role == 2):
            DEPENDENCIES = [
                (1, "SUTESUAEM"),
                (2, "FAAPA"),
                (3, "ALUMNO"),
                (4, "CONFIANZA"),
                (5, "EXTERNO")
            ] 
            if request.method == 'POST':
                form = RegisterAdminForm(request.POST)
                form.fields['dependency_id'].choices = DEPENDENCIES
                if form.is_valid():
                    admin = form.cleaned_data
                    admin.pop('password2', None)
                    admin['dependency_id'] = int(admin['dependency_id'])
                    auth_token = user_data.get('token')
                    headers = {
                        'Authorization': f'Bearer {auth_token}',
                        'Content-Type': 'application/json'
                    }
                    url_api = "https://api.ax01.dev/v1/admin/admin"
                    try:
                        response = requests.post(url_api, json=admin, headers=headers)
                        print("Status Code:", response.status_code)
                        print(admin)
                        if response.status_code == 200:
                            return HttpResponse('Registro exitoso')
                        else:
                            return HttpResponse('Registro fallido')
                    except requests.RequestException as e:
                        return HttpResponse('Error al enviar los datos')
                else:
                    return render(request, 'register_admin.html', {'register_admin_form': form})
            else:
                form = RegisterAdminForm()
                form.fields['dependency_id'].choices = DEPENDENCIES
                return render(request, 'register_admin.html', {'register_admin_form' : form})
        else:
            return HttpResponse('Permiso denegado')
    else:
        return HttpResponse('Permiso denegado')
    

def register_doctor(request):
    user_data_cookie = request.COOKIES.get('userData')
    if(user_data_cookie):
        user_data = json.loads(user_data_cookie)
        role = int(user_data.get('role'))
        if(role == 1 or role == 2):
            DEPENDENCIES = [
                (1, "SUTESUAEM"),
                (2, "FAAPA"),
                (3, "ALUMNO"),
                (4, "CONFIANZA"),
                (5, "EXTERNO")
            ]   
            if request.method == 'POST':
                form = RegisterDoctorForm(request.POST)
                form.fields['dependency_id'].choices = DEPENDENCIES
                if form.is_valid():
                    doctor = form.cleaned_data
                    doctor.pop('password2', None)
                    doctor['dependency_id'] = int(doctor['dependency_id'])
                    url_api = "https://api.ax01.dev/v1/admin/doctor"
                    auth_token = user_data.get('token')
                    headers = {
                        'Authorization': f'Bearer {auth_token}',
                        'Content-Type': 'application/json'
                    }
                    try:
                        response = requests.post(url_api, json=doctor, headers=headers)
                        print("Status Code:", response.status_code)
                        print(response.text)
                        print(doctor)
                        if response.status_code == 200:
                            return HttpResponse('Registro exitoso')
                        else:
                            return HttpResponse('Registro fallido')
                    except requests.RequestException as e:
                        return HttpResponse('Error al enviar los datos')
                else:
                    return render(request, 'register_doctor.html', {'register_doctor_form': form})
            else:
                #Estas dependencias las obtendríamos de la base de datos
                form = RegisterDoctorForm()
                form.fields['dependency_id'].choices = DEPENDENCIES
                return render(request, 'register_doctor.html', {'register_doctor_form' : form})
        else:
            return HttpResponse('Permiso denegado')
    else:
        return HttpResponse('Permiso denegado')


def register_receptionist(request):
    user_data_cookie = request.COOKIES.get('userData')
    if user_data_cookie:
        user_data = json.loads(user_data_cookie)
        role = int(user_data.get('role'))
        if role == 1 or role == 2: 
            DEPENDENCIES = [
                (1, "SUTESUAEM"),
                (2, "FAAPA"),
                (3, "ALUMNO"),
                (4, "CONFIANZA"),
                (5, "EXTERNO")
            ]
            if request.method == 'POST':
                form = RegisterReceptionistForm(request.POST)
                form.fields['dependency_id'].choices = DEPENDENCIES
                if form.is_valid():
                    form.fields.pop('password2', None)
                    receptionist = form.cleaned_data
                    receptionist['dependency_id'] = int(receptionist['dependency_id'])
                    url_api = "https://api.ax01.dev/v1/admin/receptionist"
                    auth_token = user_data.get('token')
                    headers = {
                        'Authorization': f'Bearer {auth_token}',
                        'Content-Type': 'application/json'
                    }
                    try:
                        response = requests.post(url_api, json=receptionist, headers=headers)
                        print("Status Code:", response.status_code)
                        print(response.text)
                        print(receptionist)
                        if response.status_code == 200:
                            return HttpResponse('Registro exitoso')
                        else:
                            return HttpResponse('Registro fallido')
                    except requests.RequestException as e:
                        return HttpResponse('Error al enviar los datos')
                else:
                    return render(request, 'register_receptionist.html', {'register_receptionist_form': form})
            else:
                form = RegisterReceptionistForm()
                form.fields['dependency_id'].choices = DEPENDENCIES
                return render(request, 'register_receptionist.html', {'register_receptionist_form': form})
        else:
            return HttpResponse('Permiso denegado')
    else:
        return HttpResponse('Permiso denegado')



def register_patient(request):
    user_data_cookie = request.COOKIES.get('userData')
    if user_data_cookie:
        user_data = json.loads(user_data_cookie)
        role = int(user_data.get('role'))
        if role == 1 or role == 2: 
            if request.method == 'POST':
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
                    return render(request, 'register_patient.html', {'register_patient_form': register_patient_form})
            else:
                register_patient_form = RegisterPatientForm()
                return render(request, 'register_patient.html', {'register_patient_form': register_patient_form})
        else:
            return HttpResponse('Permiso denegado')
    else:
        return HttpResponse('Permiso denegado')


def register_specialty(request):
    user_data_cookie = request.COOKIES.get('userData')
    user_data = json.loads(user_data_cookie)
    role = int(user_data.get('role'))
    auth_token = user_data.get('token')
    if (auth_token and (role == 1 or role == 2)):
        if(request.method == 'POST'):
            register_specialty_form = RegisterSpecialtyForm(request.POST)
            if register_specialty_form.is_valid():
                specialty = register_specialty_form.cleaned_data
                url_specialty = 'https://api.ax01.dev/v1/specialty'
                headers = {
                    'Authorization': f'Bearer {auth_token}',
                    'Content-Type': 'application/json'
                }
                try:
                    response = requests.post(url_specialty, json=specialty, headers=headers)
                    if response.status_code == 200:
                        return HttpResponse('Registro exitoso')
                    else:
                        return HttpResponse('Registro fallido ' + response.text)
                except requests.RequestException as e:
                        return HttpResponse('Error al enviar los datos' + e)
            else:
                return render(request, 'register_specialty.html', {'register_specialty_form' : register_specialty_form})
        else:
            register_specialty_form = RegisterSpecialtyForm()
            return render(request, 'register_specialty.html', {'register_specialty_form' : register_specialty_form})
    else:
        return HttpResponse('Permiso denegado')


def register_office(request):
    user_data_cookie = request.COOKIES.get('userData')
    user_data = json.loads(user_data_cookie)
    role = int(user_data.get('role'))
    auth_token = user_data.get('token')
    if auth_token and (role == 1 or role == 2):
        if request.method == 'POST':
            register_office_form = RegisterOfficeForm(request.POST)
            if register_office_form.is_valid():
                office = register_office_form.cleaned_data
                url_office = 'https://api.ax01.dev/v1/office'
                headers = {
                    'Authorization': f'Bearer {auth_token}',
                    'Content-Type': 'application/json'
                }
                try:
                    response = requests.post(url_office, json=office, headers=headers)
                    if response.status_code == 200:
                        return HttpResponse('Registro exitoso')
                    else:
                        return HttpResponse('Registro fallido')
                except requests.RequestException as e:
                    return HttpResponse('Error al enviar los datos')
            else:
                return render(request, 'register_office.html', {'register_office_form': register_office_form})
        else:
            register_office_form = RegisterSpecialtyForm()
            return render(request, 'register_office.html', {'register_office_form': register_office_form})
    else:
        return HttpResponse('Permiso denegado')


def register_schedule(request):
    user_data_cookie = request.COOKIES.get('userData')
    if user_data_cookie:
        user_data = json.loads(user_data_cookie)
        role = int(user_data.get('role'))
        auth_token = user_data.get('token')
        if role in [1, 2, 3]:
            url_schedule_data = 'https://api.ax01.dev/v1/admin/schedule'
            headers = {
                'Authorization': f'Bearer {auth_token}',
                'Content-Type': 'application/json'
            }
            try:
                schedule_response = requests.get(url_schedule_data, headers=headers)
                if(schedule_response.status_code == 200):
                    schedule_data = schedule_response.json()
                    data = schedule_data.get('data')
                    DAYS = [(item['id'], item['name']) for item in data.get('day_of_week', [])]
                    SHIFTS = [(item['id'], item['name']) for item in data.get('cat_shift', [])]
                    DOCTORS = [(item['account_id'], str(item['first_name'] + ' ' + item['last_name_1'] + ' ' + item['last_name_2'])) for item in data.get('doctor', [])]
                    OFFICES = [(item['office_id'], item['office_name']) for item in data.get('office', [])]
                    SERVICES = [(item['id'], item['name']) for item in data.get('cat_services', [])]
            except requests.RequestException as e:
                return HttpResponse('No se pudieron obtener los datos para crear horarios')

            if request.method == 'POST':
                register_schedule_form = RegisterScheduleForm(request.POST)
                register_schedule_form.fields['selectedDays'].choices = DAYS
                register_schedule_form.fields['officeID'].choices = OFFICES
                register_schedule_form.fields['shiftID'].choices = SHIFTS
                register_schedule_form.fields['serviceID'].choices = SERVICES
                register_schedule_form.fields['doctorID'].choices = DOCTORS

                if register_schedule_form.is_valid():
                    schedule = register_schedule_form.cleaned_data
                    timeDuration = datetime.strptime(schedule.get('timeDuration'), '%H:%M')
                    duration = timeDuration.hour * 60 + timeDuration.minute
                    timeStart = datetime.strptime(schedule.get('timeStart'), '%H:%M')
                    timeEnd = datetime.strptime(schedule.get('timeEnd'), '%H:%M')
                    timeSlots = []
                    currentTime = timeStart
                    while currentTime + timedelta(minutes=duration) <= timeEnd:
                        nextTime = currentTime + timedelta(minutes=duration)
                        timeSlots.append(f"{currentTime.strftime('%H:%M')} - {nextTime.strftime('%H:%M')}")
                        currentTime = nextTime
                    selectedDays = [int(day) for day in schedule.get('selectedDays')]
                    for day in selectedDays:
                        print(day)
                    print(timeSlots)
                    print(schedule)

                    url_api = "https://api.ax01.dev/v1/schedule"
                    try:
                        schedule_json = {
                            'selectedDays': selectedDays,
                            'timeStart': schedule.get('timeStart'),
                            'timeEnd': schedule.get('timeEnd'),
                            'timeDuration': schedule.get('timeDuration'),
                            'officeID': int(schedule.get('officeID')),
                            'shiftID': int(schedule.get('shiftID')),
                            'serviceID': int(schedule.get('serviceID')),
                            'doctorID': schedule.get('doctorID'),
                            'timeSlots': timeSlots
                        }
                        print(schedule_json)
                        response = requests.post(url_api, json=schedule_json, headers=headers)
                        print("Status Code:", response.status_code)
                        print("Response Text:", response.text)
                        if response.status_code == 200:
                            return HttpResponse('Horario creado con éxito')
                        else:
                            return HttpResponse('No se ha podido crear el horario')
                    except requests.RequestException as e:
                        return HttpResponse('Error al enviar los datos')
            else:
                register_schedule_form = RegisterScheduleForm()
                register_schedule_form.fields['selectedDays'].choices = DAYS
                register_schedule_form.fields['officeID'].choices = OFFICES
                register_schedule_form.fields['shiftID'].choices = SHIFTS
                register_schedule_form.fields['serviceID'].choices = SERVICES
                register_schedule_form.fields['doctorID'].choices = DOCTORS
                return render(request, 'register_schedule.html', {'register_schedule_form': register_schedule_form})
        else:
            return HttpResponse('Permiso denegado')
    else:
        return HttpResponse('Permiso denegado')



def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            admin = login_form.cleaned_data
            url_api = 'https://api.ax01.dev/v1/login'
            try:
                response = requests.post(url_api, json=admin)
                print('Status Code: ', response.status_code)
                print('Response Text: ', response.text)
                if response.status_code == 200:
                    response_json = response.json()
                    user_json = response_json.get('data', {})
                    role = user_json.get('role')
                    response2 = None
                    if role == 1:
                        response2 = redirect('home_superadmin')
                    elif role == 2:
                        response2 = redirect('home_admin')
                    elif role == 3:
                        response2 = redirect('home_receptionist')
                    elif role == 4:
                        response2 = redirect('home_doctor')
                    else:
                        return redirect('login')
                    response2.set_cookie('userData', json.dumps(user_json), httponly=True, secure=True, samesite='Strict')
                    return response2;
                else:
                    return render(request, 'login.html', {'login_form' : login_form})
            except requests.RequestException as e:
                return HttpResponse('Error al enviar los datos')
    else:
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form' : login_form})


def home_superadmin(request):
    user_data_cookie = request.COOKIES.get('userData')
    user_data = json.loads(user_data_cookie)
    token = user_data.get('token')
    role = int(user_data.get('role'))
    if (token and role == 1):
        return render(request, 'home_superadmin.html')
    else:
        return HttpResponse('Permiso denegado')

def home_admin(request):
    user_data_cookie = request.COOKIES.get('userData')
    user_data = json.loads(user_data_cookie)
    token = user_data.get('token')
    role = int(user_data.get('role'))
    if (token and role == 2):
        return render(request, 'home_admin.html')
    else:
        return HttpResponse('Permiso denegado')

def home_receptionist(request):
    user_data_cookie = request.COOKIES.get('userData')
    user_data = json.loads(user_data_cookie)
    token = user_data.get('token')
    role = int(user_data.get('role'))
    if (token and role == 3):
        return render(request, 'home_receptionist.html')
    else:
        return HttpResponse('Permiso denegado')


def home_doctor(request):
    user_data_cookie = request.COOKIES.get('userData')
    user_data = json.loads(user_data_cookie)
    token = user_data.get('token')
    role = int(user_data.get('role'))
    if (token and role == 4):
        return render(request, 'home_doctor.html')
    else:
        return HttpResponse('Permiso denegado')


def provide_consultation(request):
    '''
    user_data_cookie = request.COOKIES.get('userData')
    user_data = json.loads(user_data_cookie)
    token = user_data.get('token')
    role = int(user_data.get('role'))
    if (token and role):
        initial_data = ''
        medical_history_status = False
        try:
            url_api = "https://api.ax01.dev/v1/medicalh"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json' 
            }
            data_send = {'medical_history_id' : 'ASG5-391964'}
            response = requests.post(url_api, json=data_send, headers=headers)
            print(headers)
            print("Status Code:", response.status_code)
            print("Response Text:", response.text)
            if response.status_code == 200:
                print('Datos del paciente obtenidos con éxito')
                response_json = response.json()
                medical_history = response_json.get('data', {})
                medical_history_status = medical_history.get('status')
                if medical_history_status:
                    initial_data = {
                        'date_of_record': medical_history.get('date_of_record'),
                        'time_of_record': medical_history.get('time_of_record'),
                        'patient_name': medical_history.get('patient_name'),
                        'curp': medical_history.get('curp'),
                        'birth_date': medical_history.get('birth_date'),
                        'age': medical_history.get('age'),
                        'gender': medical_history.get('gender'),
                        'place_of_origin': medical_history.get('place_of_origin'),
                        'ethnic_group': medical_history.get('ethnic_group'),
                        'phone_number': medical_history.get('phone_number'),
                        'address': medical_history.get('address'),
                        'occupation': medical_history.get('occupation'),
                        'guardian_name': medical_history.get('guardian_name'),
                        'family_medical_history': medical_history.get('family_medical_history'),
                        'non_pathological_history': medical_history.get('non_pathological_history'),
                        'pathological_history': medical_history.get('pathological_history'),
                        'gynec_obstetric_history': medical_history.get('gynec_obstetric_history'),
                        'current_condition': medical_history.get('current_condition'),
                        'cardiovascular': medical_history.get('cardiovascular'),
                        'respiratory': medical_history.get('respiratory'),
                        'gastrointestinal': medical_history.get('gastrointestinal'),
                        'genitourinary': medical_history.get('genitourinary'),
                        'hematic_lymphatic': medical_history.get('hematic_lymphatic'),
                        'endocrine': medical_history.get('endocrine'),
                        'nervous_system': medical_history.get('nervous_system'),
                        'musculoskeletal': medical_history.get('musculoskeletal'),
                        'skin': medical_history.get('skin'),
                        'body_temperature': medical_history.get('body_temperature'),
                        'weight': medical_history.get('weight'),
                        'height': medical_history.get('height'),
                        'bmi': medical_history.get('bmi'),
                        'heart_rate': medical_history.get('heart_rate'),
                        'respiratory_rate': medical_history.get('respiratory_rate'),
                        'blood_pressure': medical_history.get('blood_pressure'),
                        'physical': medical_history.get('physical'),
                        'head': medical_history.get('head'),
                        'neck_and_chest': medical_history.get('neck_and_chest'),
                        'abdomen': medical_history.get('abdomen'),
                        'genital': medical_history.get('genital'),
                        'extremities': medical_history.get('extremities'),
                        'previous_results': medical_history.get('previous_results'),
                        'diagnoses': medical_history.get('diagnoses'),
                        'pharmacological_treatment': medical_history.get('pharmacological_treatment'),
                        'prognosis': medical_history.get('prognosis'),
                        'doctor_name': medical_history.get('doctor_name'),
                        'medical_license': medical_history.get('medical_license'),
                        'specialty_license': medical_history.get('specialty_license')
                    }
                else:
                    initial_data = {
                        'patient_name' : medical_history.get('patient_name'),
                        'curp' : medical_history.get('curp'),
                        'gender' : medical_history.get('gender')
                    }
            else:
                print('Error, no existe el paciente')
        except requests.RequestException as e:
            print('Error al enviar los datos')
        medical_history_form = MedicalHistoryForm(initial=initial_data)
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
    else:
        return HttpResponse("Permiso denegado")
    '''
    doc_test = {
        'name' : 'name placeholder',
        'service' : 'service placeholder',
        'license1' : 'license placeholder',
        'license2' : 'license placeholder'
    }
    medical_history_form = MedicalHistoryForm()
    evolution_note_form = EvolutionNoteForm()
    incapacity_form = IncapacityForm()
    laboratory_requisition_form = LaboratoryRequisitionForm()
    prescription_form = PrescriptionForm()
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
    auth_token = request.COOKIES.get('authToken')
    medical_history_form = MedicalHistoryForm(request.POST)
    if medical_history_form.is_valid():
        medical_history = medical_history_form.cleaned_data
        complete_medical_history = {
        "place_of_origin": medical_history.get('place_of_origin'),
        "ethnic_group": medical_history.get('ethnic_group'),
        "phone_number": medical_history.get('phone_number'),
        "address": medical_history.get('address'),
        "occupation": medical_history.get('occupation'),
        "guardian_name": medical_history.get('guardian_name'),
        "family_medical_history": medical_history.get('family_medical_history'),
        "non_pathological_history": medical_history.get('non_pathological_history'),
        "pathological_history": medical_history.get('pathological_history'),
        "gynec_obstetric_history": medical_history.get('gynec_obstetric_history'),
        "current_condition": medical_history.get('current_condition'),
        "cardiovascular": medical_history.get('cardiovascular'),
        "respiratory": medical_history.get('respiratory'),
        "gastrointestinal": medical_history.get('gastrointestinal'),
        "genitourinary": medical_history.get('genitourinary'),
        "hematic_lymphatic": medical_history.get('hematic_lymphatic'),
        "endocrine": medical_history.get('endocrine'),
        "nervous_system": medical_history.get('nervous_system'),
        "musculoskeletal": medical_history.get('musculoskeletal'),
        "skin": medical_history.get('skin'),
        "body_temperature": medical_history.get('body_temperature'),
        "weight": medical_history.get('weight'),
        "height": medical_history.get('height'),
        "bmi": medical_history.get('bmi'),
        "heart_rate": medical_history.get('heart_rate'),
        "respiratory_rate": medical_history.get('respiratory_rate'),
        "blood_pressure": medical_history.get('blood_pressure'),
        "physical": medical_history.get('physical'),
        "head": medical_history.get('head'),
        "neck_and_chest": medical_history.get('neck_and_chest'),
        "abdomen": medical_history.get('abdomen'),
        "genital": medical_history.get('genital'),
        "extremities": medical_history.get('extremities'),
        "previous_results": medical_history.get('previous_results'),
        "diagnoses": medical_history.get('diagnoses'),
        "pharmacological_treatment": medical_history.get('pharmacological_treatment'),
        "prognosis": medical_history.get('prognosis'),
        "doctor_name": medical_history.get('doctor_name'),
        "medical_license": medical_history.get('medical_license'),
        "specialty_license": medical_history.get('specialty_license'),
        "medical_history_id": medical_history.get('medical_history_id')
        }
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Content-Type': 'application/json' 
        }
        url_api = "https://api.ax01.dev/v1/medicalhc"
        response = requests.post(url_api, json=complete_medical_history, headers=headers)
        if response.status_code == 200:
            return HttpResponse("Historia médica guardada con éxito")
        else:
            return HttpResponse(f"Error al guardar la historia clínica\nStatus code:{response.status_code} Response Text:{response.text}")
    else:
            errors = medical_history_form.errors.as_json()
            return HttpResponse(errors, content_type='application/json', status=400)

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