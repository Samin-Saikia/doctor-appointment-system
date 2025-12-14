from django.db import models
from auth_app.models import User
from doctors.models import Doctor
from departments.models import Department

class TimeSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)

    class Meta:
        unique_together = ('doctor', 'date', 'start_time')
class Appointment(models.Model):
    STATUS = (
        ('BOOKED', 'Booked'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    timeslot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    token_number = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS, default='BOOKED')
    created_at = models.DateTimeField(auto_now_add=True)
class Holiday(models.Model):
    APPLY_CHOICES = (
        ('ALL', 'All'),
        ('DEPARTMENT', 'Department'),
        ('DOCTOR', 'Doctor'),
    )

    date = models.DateField()
    reason = models.CharField(max_length=255)
    applies_to = models.CharField(max_length=20, choices=APPLY_CHOICES)
    reference_id = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.doctor.name} | {self.date} | {self.start_time}"
