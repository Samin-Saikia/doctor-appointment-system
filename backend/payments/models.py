from django.db import models
from appointments.models import Appointment

class Payment(models.Model):
    STATUS = (
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    )

    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=10, choices=STATUS)
    transaction_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
