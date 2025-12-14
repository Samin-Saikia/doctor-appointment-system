# doctors/views.py

from rest_framework import viewsets
from doctors.models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()  # Fetch all doctors
    serializer_class = DoctorSerializer  # Use the serializer we just created
