from django.db import models
from departments.models import Department

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    experience_years = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
class DoctorAvailability(models.Model):
    DAYS = [
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'),
        ('SUNDAY', 'Sunday'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DAYS)
    is_active = models.BooleanField(default=True)

    # Fixing the __str__ method for better display
    def __str__(self):
        return f"{self.doctor.name} - {self.get_day_of_week_display()}"
