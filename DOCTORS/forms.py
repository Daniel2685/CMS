from django import forms
from .models import MedicalHistory, EvolutionNote, Incapacity, Patient

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
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

def no_blank_validator(value):
    if not value.strip():
        raise ValidationError("Este campo no puede estar vacío ni contener solo espacios en blanco.")

class RegisterSuperadminForm(forms.Form):
    SEX = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    first_name = forms.CharField(max_length=50, validators=[no_blank_validator], label='Nombre')
    last_name1 = forms.CharField(max_length=50, validators=[no_blank_validator], label='Apellido Paterno')
    last_name2 = forms.CharField(max_length=50, validators=[no_blank_validator], label='Apellido Materno')
    curp = forms.CharField(max_length=18, validators=[no_blank_validator], min_length=18, label='CURP')
    sex = forms.ChoiceField(choices=SEX, label='Sexo')
    phone = forms.CharField(max_length=10, min_length=10, label="Teléfono")
    email = forms.EmailField(max_length=50, label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class RegisterAdminForm(forms.Form):
    SEX = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    first_name = forms.CharField(max_length=50, validators=[no_blank_validator], label='Nombre')
    last_name1 = forms.CharField(max_length=50, validators=[no_blank_validator], label='Apellido Paterno')
    last_name2 = forms.CharField(max_length=50, validators=[no_blank_validator], label='Apellido Materno')
    curp = forms.CharField(max_length=18, validators=[no_blank_validator], min_length=18, label='CURP')
    sex = forms.ChoiceField(choices=SEX, label='Sexo')
    phone = forms.CharField(max_length=10, min_length=10, label="Teléfono")
    email = forms.EmailField(max_length=50, label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class RegisterDoctorForm(forms.Form):
    SEX = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    dependency_id = forms.ChoiceField(choices=[], label='Dependencia')
    medical_license = forms.CharField(min_length=8, max_length=8, label="Cédula Profesional")
    specialty_id = forms.ChoiceField(choices=[], label="Especialidad")
    name = forms.CharField(max_length=50, validators=[no_blank_validator], label="Nombre")
    last_name1 = forms.CharField(max_length=50, validators=[no_blank_validator], label="Apellido Paterno")
    last_name2 = forms.CharField(max_length=50, validators=[no_blank_validator], label="Apellido Materno")
    #speciality_license = forms.CharField(min_length=8, max_length=8, label="Cédula de Especialidad")
    sex = forms.ChoiceField(choices=SEX, label='Sexo')
    phone = forms.CharField(max_length=10, min_length=10, label="Teléfono")
    email = forms.EmailField(max_length=50, label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class RegisterReceptionistForm(forms.Form):
    SEX = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    first_name = forms.CharField(max_length=50, validators=[no_blank_validator], label='Nombre')
    last_name1 = forms.CharField(max_length=50, validators=[no_blank_validator], label='Apellido Paterno')
    last_name2 = forms.CharField(max_length=50, validators=[no_blank_validator], label='Apellido Materno')
    curp = forms.CharField(max_length=18, validators=[no_blank_validator], min_length=18, label='CURP')
    sex = forms.ChoiceField(choices=SEX, label='Sexo')
    phone = forms.CharField(max_length=10, min_length=10, label="Teléfono")
    email = forms.EmailField(max_length=50, label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class RegisterScheduleForm(forms.Form):
    DURATIONS = [
        ('01:00', '1 hora'),
        ('00:45', '45 minutos'),
        ('00:30', '30 minutos')
    ]

    SHIFTS = [
        (1, 'Matutino'),
        (2, 'Vespertino')
    ]

    SERVICES = [
        (1, "Medicina General"),
        (2, "Pediatría"),
        (3, "Ginecología")
    ]

    HOURS = [(f"{hora:02d}:00", f"{hora:02d}:00") for hora in range(7, 21)]

    DAYS = [
    (1, 'Lunes'),
    (2, 'Martes'),
    (3, 'Miércoles'),
    (4, 'Jueves'),
    (5, 'Viernes'),
    (6, 'Sábado'),
    ]

    selectedDays =  forms.MultipleChoiceField(choices=DAYS, widget=forms.CheckboxSelectMultiple, label='Días de la semana')
    timeStart = forms.ChoiceField(choices=HOURS, label='Hora de inicio')
    timeEnd = forms.ChoiceField(choices=HOURS, label='Hora de término')
    timeDuration = forms.ChoiceField(choices=DURATIONS, label='Duración')
    officeID = forms.CharField(max_length=2, label='Número consultorio')
    shiftID = forms.ChoiceField(choices=SHIFTS, label='Turno')
    serviceID = forms.ChoiceField(choices=SERVICES, label='Servicio')
    doctorID = forms.CharField(max_length=36, label='ID Doctor')

'''

class RegisterScheduleForm(forms.Form):
    selectedDays #Esto es una lista de enteros que pueden ir de 1 a 7 para los dias de la semana
    timeStart #Esto es para definir el tiempo de inicio
    timeEnd #Esto es para definir el tiempo de finalizacion
    timeDuration #Esto es para definir la duracion
    shiftID #numero del 1 al 2 para ver si es matutino o vespertino
    serviceID #esto simplemente es del servicio
    doctorID #el id del doctor
    officeID #el id del consultorio
    timeSlots #los tiempos generados, lista de strings de fecha con formato ["09:00 - 10:00", "10:00 - 11:00"]
'''


class DoctorLoginForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    

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

class LaboratoryRequisitionForm(forms.Form):
    folio = forms.CharField(label='Folio', max_length=50)
    patient_name = forms.CharField(label='Nombre del paciente', max_length=50)
    curp = forms.CharField(label='CURP', max_length=18)
    age = forms.CharField(label='Edad', max_length=3)
    date = forms.DateField(label='Fecha', widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'fecha'}))
    sex = forms.CharField(label='Sexo', max_length=10)
    tests = forms.CharField(label='Exámenes a realizar', max_length=100)

class PrescriptionForm(forms.Form):
    patient_name = forms.CharField(label='Nombre', max_length=50, initial='', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    curp = forms.CharField(label='CURP', max_length=18, initial='', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    age = forms.CharField(label='Edad', max_length=3)
    date = forms.DateField(label='Fecha', widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'fecha'}))
    temperature = forms.CharField(label='Temperatura')
    weight = forms.CharField(label='Peso')
    height = forms.CharField(label='Talla')
    bmi = forms.CharField(label='IMC')
    blood_pressure = forms.CharField(label='TA')
    heart_rate = forms.CharField(label='FC')
    respiratory_rate = forms.CharField(label='FR')
    oxygen_saturation = forms.CharField(label='SO2')
    alergies = forms.CharField(label='Alergias')
    prescription = forms.CharField(label='Prescripción')

class DoctorLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())