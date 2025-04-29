from django.db import models


class Doctor(models.Model):
    first_name = models.CharField('Nombre',max_length=100)
    last_name = models.CharField('Apellido',max_length=100)
    qualification = models.CharField('Calificacion',max_length=100)
    contact_number = models.CharField('Numero de contacto',max_length=15)
    email = models.EmailField()
    address = models.TextField('Direccion')
    biography = models.TextField('Biografia')
    is_on_vacation = models.BooleanField('Esta de vacaciones?',default=False)


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(
        Doctor, related_name='availabilities', on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class MedicalNote(models.Model):
    doctor = models.ForeignKey(
        Doctor, related_name='medical_notes', on_delete=models.CASCADE
    )
    note = models.TextField()
    date = models.DateField()
