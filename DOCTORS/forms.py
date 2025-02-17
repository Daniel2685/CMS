from django import forms
from .models import MedicalHistory, EvolutionNote, Incapacity, Patient
import csv

cie_diagnosis = 'diagnosticos_cie.csv'

def load_diagnosis_from_csv(csv_file):
    choices = []
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                # Formar la tupla (código, "código + nombre")
                choices.append((row[0], f"{row[0]} - {row[1]}"))
    return choices

def load_pharma_from_csv(csv_file):
    choices = []
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 6:
                # Formar la tupla (código, "código + nombre")
                choices.append((row[0], f"{row[0]}. {row[3]}. {row[1]}. {row[2]}. {row[4]} cada {row[5]}"))
    return choices

diagnosis = load_diagnosis_from_csv(cie_diagnosis)
pharma = load_pharma_from_csv('lista_medicamentos.csv')

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['account', 'medical_history']
        labels = {
            'legacy_id': 'ID legado',
            'first_name': 'Nombre',
            'last_name1': 'Primer apellido',
            'last_name2': 'Segundo apellido',
            'curp': 'CURP',
            'sex': 'Sexo',
            'created_at': 'Fecha de creación',
            'updated_at': 'Fecha de actualización',
            'deleted_at': 'Fecha de eliminación',
        }

class RegisterPatientForm(forms.Form):
    DEPENDENCIES = [
        (1, "SUTESUAEM"),
        (2, "FAAPA"),
        (3, "ALUMNO"),
        (4, "CONFIANZA"),
        (5, "EXTERNO")
    ]
    SEX = [
        ("M", "Masculino"),
        ("F", "Femenino")
    ]
    dependency_id = forms.ChoiceField(choices=DEPENDENCIES, label="Dependencia")
    name = forms.CharField(max_length=50, label="Nombre")
    lastname1 = forms.CharField(max_length=50, label="Apellido Paterno")
    lastname2 = forms.CharField(max_length=50, label="Apellido Materno")
    curp = forms.CharField(max_length=18, min_length=18, label="CURP")
    sex = forms.ChoiceField(choices=SEX, label="Sexo")
    phone = forms.CharField(max_length=10, min_length=10, label="Teléfono")
    email = forms.EmailField(max_length=50, label="Correo electrónico")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password-field'}), 
        label="Contraseña"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password-field'}), 
        label="Confirmar contraseña"
    )

def no_blank_validator(value):
    if not value.strip():
        raise ValidationError("Este campo no puede estar vacío ni contener solo espacios en blanco.")

class RegisterSuperadminForm(forms.Form):
    SEX = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    dependency_id = forms.ChoiceField(choices=[], label='Dependencia')
    name = forms.CharField(max_length=50, validators=[no_blank_validator], label='Nombre')
    lastname1 = forms.CharField(max_length=50, validators=[no_blank_validator], label='Apellido Paterno')
    lastname2 = forms.CharField(max_length=50, validators=[no_blank_validator], label='Apellido Materno')
    curp = forms.CharField(max_length=18, validators=[no_blank_validator], min_length=18, label='CURP')
    sex = forms.ChoiceField(choices=SEX, label='Sexo')
    phone = forms.CharField(max_length=10, min_length=10, label="Teléfono")
    email = forms.EmailField(max_length=50, label="Correo electrónico")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password-field'}), 
        label="Contraseña"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password-field'}), 
        label="Confirmar contraseña"
    )

class RegisterAdminForm(forms.Form):
    SEX = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    dependency_id = forms.ChoiceField(choices=[], label='Dependencia')
    name = forms.CharField(max_length=50, validators=[no_blank_validator], label='Nombre')
    lastname1 = forms.CharField(max_length=50, validators=[no_blank_validator], label='Apellido Paterno')
    lastname2 = forms.CharField(max_length=50, validators=[no_blank_validator], label='Apellido Materno')
    curp = forms.CharField(max_length=18, validators=[no_blank_validator], min_length=18, label='CURP')
    sex = forms.ChoiceField(choices=SEX, label='Sexo')
    phone = forms.CharField(max_length=10, min_length=10, label="Teléfono")
    email = forms.EmailField(max_length=50, label="Correo electrónico")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password-field'}), 
        label="Contraseña"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password-field'}), 
        label="Confirmar contraseña"
    )

class RegisterDoctorForm(forms.Form):
    SEX = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    dependency_id = forms.ChoiceField(choices=[], label='Dependencia')
    medical_license = forms.CharField(max_length=8, label="Cédula Profesional")
    #specialty_id = forms.ChoiceField(choices=[], label="Especialidad")
    name = forms.CharField(max_length=50, validators=[no_blank_validator], label="Nombre")
    lastname1 = forms.CharField(max_length=50, validators=[no_blank_validator], label="Apellido Paterno")
    lastname2 = forms.CharField(max_length=50, validators=[no_blank_validator], label="Apellido Materno")
    #speciality_license = forms.CharField(min_length=8, max_length=8, label="Cédula de Especialidad")
    sex = forms.ChoiceField(choices=SEX, label='Sexo')
    phone = forms.CharField(max_length=10, min_length=10, label="Teléfono")
    email = forms.EmailField(max_length=50, label="Correo electrónico")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password-field'}), 
        label="Contraseña"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password-field'}), 
        label="Confirmar contraseña"
    )

class RegisterReceptionistForm(forms.Form):
    SEX = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    dependency_id = forms.ChoiceField(choices=[], label='Dependencia')
    name = forms.CharField(max_length=50, validators=[no_blank_validator], label='Nombre')
    lastname1 = forms.CharField(max_length=50, validators=[no_blank_validator], label='Apellido Paterno')
    lastname2 = forms.CharField(max_length=50, validators=[no_blank_validator], label='Apellido Materno')
    curp = forms.CharField(max_length=18, validators=[no_blank_validator], min_length=18, label='CURP')
    sex = forms.ChoiceField(choices=SEX, label='Sexo')
    phone = forms.CharField(max_length=10, min_length=10, label="Teléfono")
    email = forms.EmailField(max_length=50, label="Correo electrónico")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password-field'}), 
        label="Contraseña"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'password-field'}), 
        label="Confirmar contraseña"
    )

class RegisterScheduleForm(forms.Form):
    DURATIONS = [
        ('01:00', '1 hora'),
        ('00:45', '45 minutos'),
        ('00:30', '30 minutos')
    ]

    HOURS = [(f"{hora:02d}:00", f"{hora:02d}:00") for hora in range(7, 21)]

    selectedDays =  forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple, label='Días de la semana')
    timeStart = forms.ChoiceField(choices=HOURS, label='Hora de inicio')
    timeEnd = forms.ChoiceField(choices=HOURS, label='Hora de término')
    timeDuration = forms.ChoiceField(choices=DURATIONS, label='Duración')
    officeID = forms.ChoiceField(choices=[], label='Número consultorio')
    shiftID = forms.ChoiceField(choices=[], label='Turno')
    serviceID = forms.ChoiceField(choices=[], label='Servicio')
    doctorID = forms.ChoiceField(choices=[], label='ID Doctor')

class RegisterSpecialtyForm(forms.Form):
    name = forms.CharField(max_length=50, validators=[no_blank_validator], label='Nombre')

class RegisterOfficeForm(forms.Form):
    name = forms.CharField(max_length=50, validators=[no_blank_validator], label='Nombre')


class DoctorLoginForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")

class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")


class MedicalHistoryForm(forms.Form):
    id = forms.CharField(max_length=12, required=True)
    date_of_record = forms.DateField(required=False, label='Fecha de registro')
    time_of_record = forms.TimeField(required=False, label='Hora de registro')
    patient_name = forms.CharField(max_length=50, required=True, label='Nombre')
    curp = forms.CharField(max_length=18, required=True, label='CURP')
    birth_date = forms.DateField(required=False, label='Fecha de nacimiento')
    age = forms.CharField(max_length=3, required=False, label='Edad')
    gender = forms.CharField(max_length=10, required=True, label='Sexo')
    place_of_origin = forms.CharField(max_length=10, required=False, label='Lugar de origen')
    ethnic_group = forms.CharField(max_length=20, required=False, label='Grupo étnico')
    phone_number = forms.CharField(max_length=10, required=False, label='Número de teléfono')
    other_affiliation = forms.ChoiceField(choices=[], label='Derechohabiencia')
    address = forms.CharField(max_length=50, required=False, label='Dirección')
    occupation = forms.CharField(max_length=20, required=False, label='Ocupación')
    guardian_name = forms.CharField(max_length=50, required=False, label='Nombre del tutor')
    history = forms.CharField(max_length=100, required=False, label='Antecedentes')
    family_medical_history = forms.CharField(max_length=100, required=False, label='Antecedentes médicos familiares')
    non_pathological_history = forms.CharField(max_length=100, required=False, label='Antecedentes no patológicos')
    pathological_history = forms.CharField(max_length=100, required=False, label='Antecedentes patológicos')
    gynec_obstetric_history = forms.CharField(max_length=100, required=False, label='Antecedentes gineco-obstétricos')
    interrogatory = forms.CharField(max_length=100, required=False, label='Interrogatorio por aparatos y sistemas')
    cardiovascular = forms.CharField(max_length=100, required=False, label='Sistema cardiovascular')
    respiratory = forms.CharField(max_length=100, required=False, label='Sistema respiratorio')
    gastrointestinal = forms.CharField(max_length=100, required=False, label='Sistema gastrointestinal')
    genitourinary = forms.CharField(max_length=100, required=False, label='Sistema genitourinario')
    hematic_lymphatic = forms.CharField(max_length=100, required=False, label='Sistema hemático y linfático')
    endocrine = forms.CharField(max_length=100, required=False, label='Sistema endocrino')
    nervous_system = forms.CharField(max_length=100, required=False, label='Sistema nervioso')
    musculoskeletal = forms.CharField(max_length=100, required=False, label='Sistema musculoesquelético')
    physical = forms.CharField(max_length=100, required=False, label='Examen físico')
    skin = forms.CharField(max_length=100, required=False, label='Piel')
    body_temperature = forms.CharField(max_length=10, required=False, label='Temperatura corporal')
    weight = forms.CharField(max_length=5, required=False, label='Peso')
    height = forms.CharField(max_length=10, required=False, label='Altura')
    bmi = forms.CharField(max_length=10, required=False, label='Índice de masa corporal (IMC)')
    heart_rate = forms.CharField(max_length=10, required=False, label='Frecuencia cardíaca')
    respiratory_rate = forms.CharField(max_length=10, required=False, label='Frecuencia respiratoria')
    blood_pressure = forms.CharField(max_length=10, required=False, label='Presión arterial')
    head_and_neck= forms.CharField(max_length=100, required=False, label='Cabeza y Cuello')
    chest = forms.CharField(max_length=100, required=False, label='Tórax')
    abdomen = forms.CharField(max_length=100, required=False, label='Abdomen')
    genital = forms.CharField(max_length=100, required=False, label='Genitales')
    extremities = forms.CharField(max_length=100, required=False, label='Extremidades')
    previous_results = forms.CharField(max_length=100, required=False, label='Resultados de gabinete')
    motive = forms.CharField(max_length=100, required=False, label='Motivo')
    diagnoses_options = forms.ChoiceField(choices=diagnosis, label='Seleccionar diagnóstico/s')
    diagnoses = forms.CharField(max_length=1000, label='Diagnósticos', widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))
    pharma_options = forms.ChoiceField(choices=pharma, label='Seleccionar tratamiento/s')
    pharmacological_treatment = forms.CharField(max_length=1000, label='Tratamiento farmacológico', widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))
    prognosis = forms.CharField(max_length=100, required=False, label='Pronóstico')
    doctor_name = forms.CharField(max_length=50, required=False, label='Nombre del médico')
    medical_license = forms.CharField(max_length=10, required=False, label='Cédula médica')
    specialty_license = forms.CharField(max_length=10, required=False, label='Cédula de especialidad')

    
'''
class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = '__all__'
        exclude = ['id']
        labels = {
            'date_of_record': 'Fecha de registro',
            'time_of_record': 'Hora de registro',
            'patient_name': 'Nombre del paciente',
            'curp': 'CURP',
            'birth_date': 'Fecha de nacimiento',
            'age': 'Edad',
            'gender': 'Género',
            'place_of_origin': 'Lugar de origen',
            'ethnic_group': 'Grupo étnico',
            'phone_number': 'Número de teléfono',
            'address': 'Dirección',
            'occupation': 'Ocupación',
            'guardian_name': 'Nombre del tutor',
            'family_medical_history': 'Antecedentes médicos familiares',
            'non_pathological_history': 'Antecedentes no patológicos',
            'pathological_history': 'Antecedentes patológicos',
            'gynec_obstetric_history': 'Antecedentes gineco-obstétricos',
            'current_condition': 'Condición actual',
            'cardiovascular': 'Sistema cardiovascular',
            'respiratory': 'Sistema respiratorio',
            'gastrointestinal': 'Sistema gastrointestinal',
            'genitourinary': 'Sistema genitourinario',
            'hematic_lymphatic': 'Sistema hemático y linfático',
            'endocrine': 'Sistema endocrino',
            'nervous_system': 'Sistema nervioso',
            'musculoskeletal': 'Sistema musculoesquelético',
            'skin': 'Piel',
            'body_temperature': 'Temperatura corporal',
            'weight': 'Peso',
            'height': 'Altura',
            'bmi': 'Índice de masa corporal (IMC)',
            'heart_rate': 'Frecuencia cardíaca',
            'respiratory_rate': 'Frecuencia respiratoria',
            'blood_pressure': 'Presión arterial',
            'physical': 'Examen físico',
            'head': 'Cabeza',
            'neck_and_chest': 'Cuello y tórax',
            'abdomen': 'Abdomen',
            'genital': 'Genitales',
            'extremities': 'Extremidades',
            'previous_results': 'Resultados anteriores',
            'diagnoses': 'Diagnósticos',
            'pharmacological_treatment': 'Tratamiento farmacológico',
            'prognosis': 'Pronóstico',
            'doctor_name': 'Nombre del médico',
            'medical_license': 'Cédula médica',
            'specialty_license': 'Cédula de especialidad',
        }
'''
'''
class EvolutionNoteForm(forms.ModelForm):
    class Meta:
        model = EvolutionNote
        fields = '__all__'
        labels = {
            'folio': 'Folio',
            'date': 'Fecha',
            'name': 'Nombre',
            'curp': 'CURP',
            'department': 'Departamento',
            'affiliation': 'Afiliación',
            'age': 'Edad',
            'weight': 'Peso',
            'height': 'Altura',
            'heart_rate': 'Frecuencia cardíaca',
            'respiratory_rate': 'Frecuencia respiratoria',
            'blood_pressure': 'Presión arterial',
            'temperature': 'Temperatura',
            'spo2': 'SpO2',
            'glucose': 'Glucosa',
            'notes': 'Notas',
        }
'''

class EvolutionNoteForm(forms.Form):
    id = forms.CharField(max_length=12, required=True)
    date_of_record = forms.DateField(required=False, label='Fecha de registro')
    patient_name = forms.CharField(max_length=50, required=True, label='Nombre')
    curp = forms.CharField(max_length=18, required=True, label='CURP')
    service = forms.CharField(max_length=20, required=False, label='Servicio')
    affiliation = forms.ChoiceField(choices=[], label='Derechohabiencia')
    age = forms.CharField(max_length=3, required=False, label='Edad')
    wight = forms.CharField(max_length=5, required=False, label='Peso')
    height = forms.CharField(max_length=10, required=False, label='Altura')
    heart_rate = forms.CharField(max_length=10, required=False, label='Frecuencia cardíaca')
    respiratory_rate = forms.CharField(max_length=10, required=False, label='Frecuencia respiratoria')
    blood_pressure = forms.CharField(max_length=10, required=False, label='Presión arterial')
    temperature = forms.CharField(max_length=10, required=False, label='Temperatura corporal')
    spo2 = forms.CharField(max_length=10, required=False, label='SPo2')
    glucose = forms.CharField(max_length=10, required=False, label='Glucosa')
    motive = forms.CharField(max_length=100, required=False, label='Motivo')
    diagnoses_options = forms.ChoiceField(choices=diagnosis, label='Seleccionar diagnóstico/s')
    diagnoses = forms.CharField(max_length=1000, label='Diagnósticos', widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))
    pharma_options = forms.ChoiceField(choices=pharma, label='Seleccionar tratamiento/s')
    pharmacological_treatment = forms.CharField(max_length=1000, label='Tratamiento farmacológico', widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))
        
'''
class IncapacityForm(forms.ModelForm):
    class Meta:
        model = Incapacity
        fields = '__all__'
        labels = {
            'folio': 'Folio',
            'date': 'Fecha',
            'name': 'Nombre',
            'curp': 'CURP',
            'department': 'Departamento',
            'assigned_to': 'Asignado a',
            'total_days': 'Total de días',
            'start_incapacity': 'Fecha de inicio de incapacidad',
            'end_incapacity': 'Fecha de fin de incapacidad',
            'doctor': 'Nombre del médico',
            'service': 'Servicio',
            'key_code': 'Código clave',
        }
'''

class IncapacityForm(forms.Form):
    #folio = forms.CharField(label='Folio', max_length=50)
    date_of_record = forms.CharField(required=False, label='Fecha de registro')
    patient_name = forms.CharField(max_length=50, required=True, label='Nombre')
    curp = forms.CharField(max_length=18, required=True, label='CURP')
    service = forms.CharField(max_length=20, required=False, label='Servicio')
    assigned_to = forms.CharField(label='Adscrito a', max_length=50)
    affiliation = forms.ChoiceField(choices=[], label='Derechohabiencia', required=False)
    start_incapacity = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}), label='A partir del')
    end_incapacity = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}), label='Hasta el')
    total_days = forms.CharField(max_length=3, label='Días autorizados')
    diagnoses = forms.CharField(max_length=1000, label='Diagnósticos', widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))
    doctor_name = forms.CharField(max_length=50, required=True, label='Nombre del médico')
    key = forms.CharField(max_length=50, required=True, label='Clave')


class LaboratoryRequisitionForm(forms.Form):
    folio = forms.CharField(label='Folio', max_length=50)
    patient_name = forms.CharField(label='Nombre del paciente', max_length=50)
    curp = forms.CharField(label='CURP', max_length=18)
    age = forms.CharField(label='Edad', max_length=3)
    date_of_record = forms.DateField(label='Fecha', widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'fecha'}))
    sex = forms.CharField(label='Sexo', max_length=10)
    tests = forms.CharField(label='Exámenes a realizar', max_length=100)

class PrescriptionForm(forms.Form):
    patient_name = forms.CharField(label='Nombre', initial='', widget=forms.TextInput(attrs={})) #'readonly': 'readonly'
    curp = forms.CharField(label='CURP', max_length=18, initial='', widget=forms.TextInput(attrs={}))
    age = forms.CharField(label='Edad', max_length=3)
    date_of_record = forms.CharField(label='Fecha', widget=forms.TextInput(attrs={'class': 'fecha'}))
    temperature = forms.CharField(label='Temperatura')
    weight = forms.CharField(label='Peso')
    height = forms.CharField(label='Talla')
    bmi = forms.CharField(label='IMC')
    blood_pressure = forms.CharField(label='TA')
    heart_rate = forms.CharField(label='FC')
    ventricullar_fibrillation = forms.CharField(label='FV')
    respiratory_rate = forms.CharField(label='FR')
    oxygen_saturation = forms.CharField(label='SO2')
    allergies = forms.CharField(label='Alergias')
    diagnoses = forms.CharField(max_length=1000, label='Diagnósticos', widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))
    prescription = forms.CharField(max_length=1000, label='Tratamiento farmacológico', widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}))

class DoctorLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())