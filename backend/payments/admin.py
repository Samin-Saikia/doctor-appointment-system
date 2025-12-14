from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'amount', 'payment_method', 'payment_status', 'transaction_id', 'created_at')
    list_filter = ('payment_status', 'payment_method')
    search_fields = ('appointment__user__username', 'transaction_id')

admin.site.register(Payment, PaymentAdmin)
