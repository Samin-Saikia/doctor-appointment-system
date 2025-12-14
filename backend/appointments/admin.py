from django.contrib import admin
from .models import Appointment, TimeSlot, Holiday
from django import forms

# TimeSlot form with 12-hour clock
class TimeSlotAdminForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = '__all__'
        widgets = {
            'start_time': forms.TimeInput(format='%I:%M %p'),
            'end_time': forms.TimeInput(format='%I:%M %p'),
        }

class TimeSlotAdmin(admin.ModelAdmin):
    form = TimeSlotAdminForm
    list_display = ('doctor', 'date', 'start_time', 'end_time', 'is_booked', 'is_disabled')
    list_filter = ('doctor', 'date', 'is_booked', 'is_disabled')
    search_fields = ('doctor__name',)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'doctor', 'department', 'timeslot', 'appointment_date', 'status', 'token_number')
    list_filter = ('status', 'department')
    search_fields = ('user__username', 'doctor__name')

class HolidayAdmin(admin.ModelAdmin):
    list_display = ('date', 'reason', 'applies_to', 'reference_id', 'is_active')
    list_filter = ('applies_to', 'is_active')
    search_fields = ('reason',)

admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Holiday, HolidayAdmin)
