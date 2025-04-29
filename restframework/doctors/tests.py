from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from patients.models import Patient
from doctors.models import Doctor


class DoctorViewSetTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='Roberto',
            last_name='Ramos',
            date_of_birth='2003-09-16',
            contact_number='6344-7788',
            email='rober.ramos@gmail.com',
            address='Panama',
            medical_history='estudiante de medicina',
        )
        self.doctor = Doctor.objects.create(
            first_name='Carlos',
            last_name='Herrera',
            qualification='Profesional',
            contact_number='4453-6442',
            email='carlosH@gmail.com',
            address='Panama Oeste',
            biography='Sin',
            is_on_vacation=False,
        )
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse(
            'doctor-appointments',
            kwargs={"pk": self.doctor.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
