# doctors/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doctors.views import DoctorViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)  # Register the API viewset with a URL

urlpatterns = [
    path('api/', include(router.urls)),  # This makes the API available at /api/doctors/
]
