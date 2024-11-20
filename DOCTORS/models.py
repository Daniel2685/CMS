# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    id = models.UUIDField(primary_key=True)
    dependency = models.ForeignKey('CatDependencies', models.DO_NOTHING)
    phone = models.CharField(max_length=10)
    email = models.CharField(unique=True, max_length=75)
    password = models.CharField(max_length=255)
    role = models.ForeignKey('CatRole', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    password_change_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class Appointment(models.Model):
    id = models.UUIDField(primary_key=True)
    doctor = models.ForeignKey('Doctor', models.DO_NOTHING)
    patient_account = models.ForeignKey('Patient', models.DO_NOTHING)
    office = models.ForeignKey('Office', models.DO_NOTHING)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    schedule = models.ForeignKey('Schedule', models.DO_NOTHING)
    status = models.ForeignKey('AppointmentStatus', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointment'


class AppointmentStatus(models.Model):
    name = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointment_status'


class Beneficiary(models.Model):
    id = models.UUIDField(primary_key=True)
    account_holder = models.ForeignKey('Patient', models.DO_NOTHING, db_column='account_holder')
    medical_history = models.ForeignKey('MedicalHistory', models.DO_NOTHING)
    first_name = models.CharField(max_length=50)
    last_name1 = models.CharField(max_length=50)
    last_name2 = models.CharField(max_length=50)
    curp = models.CharField(max_length=18)
    sex = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beneficiary'


class CatDependencies(models.Model):
    name = models.CharField(max_length=70, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_dependencies'


class CatRole(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_role'


class Consultation(models.Model):
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    symptoms = models.TextField()
    doctor_notes = models.TextField(blank=True, null=True)
    requested_tests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consultation'


class Doctor(models.Model):
    account = models.OneToOneField(Account, models.DO_NOTHING, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name1 = models.CharField(max_length=50)
    last_name2 = models.CharField(max_length=50)
    specialty = models.ForeignKey('Specialty', models.DO_NOTHING)
    medical_license = models.CharField(max_length=25)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class EvolutionNote(models.Model):
    folio = models.AutoField(primary_key=True)
    date = models.DateField()
    name = models.CharField(max_length=50)
    curp = models.CharField(max_length=18)
    department = models.CharField(max_length=15, blank=True, null=True)
    affiliation = models.CharField(max_length=15, blank=True, null=True)
    age = models.CharField(max_length=3)
    weight = models.CharField(max_length=6)
    height = models.CharField(max_length=6)
    heart_rate = models.CharField(max_length=6)
    respiratory_rate = models.CharField(max_length=6)
    blood_pressure = models.CharField(max_length=6)
    temperature = models.CharField(max_length=6)
    spo2 = models.CharField(max_length=6)
    glucose = models.CharField(max_length=6)
    notes = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'evolution_note'


class Incapacity(models.Model):
    folio = models.AutoField(primary_key=True)
    date = models.DateField()
    name = models.CharField(max_length=50)
    curp = models.CharField(max_length=18)
    department = models.CharField(max_length=15, blank=True, null=True)
    assigned_to = models.CharField(max_length=15, blank=True, null=True)
    total_days = models.CharField(max_length=3)
    start_incapacity = models.DateField()
    end_incapacity = models.DateField()
    doctor = models.CharField(max_length=50)
    service = models.CharField(max_length=20)
    key_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'incapacity'


class MedicalHistory(models.Model):
    id = models.CharField(primary_key=True, max_length=12)
    date_of_record = models.DateField(blank=True, null=True)
    time_of_record = models.TimeField(blank=True, null=True)
    patient_name = models.CharField(max_length=50)
    curp = models.CharField(max_length=18)
    birth_date = models.DateField(blank=True, null=True)
    age = models.CharField(max_length=3, blank=True, null=True)
    gender = models.CharField(max_length=10)
    place_of_origin = models.CharField(max_length=10, blank=True, null=True)
    ethnic_group = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=20, blank=True, null=True)
    guardian_name = models.CharField(max_length=50, blank=True, null=True)
    family_medical_history = models.CharField(max_length=100, blank=True, null=True)
    non_pathological_history = models.CharField(max_length=100, blank=True, null=True)
    pathological_history = models.CharField(max_length=100, blank=True, null=True)
    gynec_obstetric_history = models.CharField(max_length=100, blank=True, null=True)
    current_condition = models.CharField(max_length=100, blank=True, null=True)
    cardiovascular = models.CharField(max_length=100, blank=True, null=True)
    respiratory = models.CharField(max_length=100, blank=True, null=True)
    gastrointestinal = models.CharField(max_length=100, blank=True, null=True)
    genitourinary = models.CharField(max_length=100, blank=True, null=True)
    hematic_lymphatic = models.CharField(max_length=100, blank=True, null=True)
    endocrine = models.CharField(max_length=100, blank=True, null=True)
    nervous_system = models.CharField(max_length=100, blank=True, null=True)
    musculoskeletal = models.CharField(max_length=100, blank=True, null=True)
    skin = models.CharField(max_length=100, blank=True, null=True)
    body_temperature = models.CharField(max_length=10, blank=True, null=True)
    weight = models.CharField(max_length=5, blank=True, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
    bmi = models.CharField(max_length=10, blank=True, null=True)
    heart_rate = models.CharField(max_length=10, blank=True, null=True)
    respiratory_rate = models.CharField(max_length=10, blank=True, null=True)
    blood_pressure = models.CharField(max_length=10, blank=True, null=True)
    physical = models.CharField(max_length=100, blank=True, null=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    neck_and_chest = models.CharField(max_length=100, blank=True, null=True)
    abdomen = models.CharField(max_length=100, blank=True, null=True)
    genital = models.CharField(max_length=100, blank=True, null=True)
    extremities = models.CharField(max_length=100, blank=True, null=True)
    previous_results = models.CharField(max_length=100, blank=True, null=True)
    diagnoses = models.CharField(max_length=100, blank=True, null=True)
    pharmacological_treatment = models.CharField(max_length=100, blank=True, null=True)
    prognosis = models.CharField(max_length=100, blank=True, null=True)
    doctor_name = models.CharField(max_length=50, blank=True, null=True)
    medical_license = models.CharField(max_length=10, blank=True, null=True)
    specialty_license = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_history'


class MedicalHistoryRelation(models.Model):
    id = models.UUIDField(primary_key=True)
    medical_history = models.ForeignKey(MedicalHistory, models.DO_NOTHING)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)
    beneficiary = models.ForeignKey(Beneficiary, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_history_relation'


class Office(models.Model):
    name = models.CharField(max_length=60)
    specialty = models.ForeignKey('Specialty', models.DO_NOTHING)
    status = models.ForeignKey('OfficeStatus', models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'office'


class OfficeStatus(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'office_status'


class Patient(models.Model):
    account = models.OneToOneField(Account, models.DO_NOTHING, primary_key=True)
    medical_history = models.ForeignKey(MedicalHistory, models.DO_NOTHING)
    legacy_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name1 = models.CharField(max_length=50)
    last_name2 = models.CharField(max_length=50)
    curp = models.CharField(max_length=18)
    sex = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class Permissions(models.Model):
    name = models.CharField(unique=True, max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class Recepcionista(models.Model):
    account_id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name1 = models.CharField(max_length=50)
    last_name2 = models.CharField(max_length=50)
    curp = models.CharField(max_length=18)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recepcionista'


class RolePermission(models.Model):
    role = models.OneToOneField(CatRole, models.DO_NOTHING, primary_key=True)  # The composite primary key (role_id, permission_id) found, that is not supported. The first column is selected.
    permission = models.ForeignKey(Permissions, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_permission'
        unique_together = (('role', 'permission'),)


class Schedule(models.Model):
    office = models.ForeignKey(Office, models.DO_NOTHING)
    day_of_week = models.IntegerField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'


class Services(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'


class Specialty(models.Model):
    name = models.CharField(max_length=75)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specialty'


class SuperAdmin(models.Model):
    account = models.OneToOneField(Account, models.DO_NOTHING, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name1 = models.CharField(max_length=50)
    last_name2 = models.CharField(max_length=50)
    curp = models.CharField(max_length=18)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'super_admin'


class UserRoles(models.Model):
    account = models.ForeignKey(Account, models.DO_NOTHING)
    role = models.ForeignKey(CatRole, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_roles'
        unique_together = (('account', 'role'),)
