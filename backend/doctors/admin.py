# doctors/admin.py (Display all available days in a single column)

from django.contrib import admin
from .models import Doctor, DoctorAvailability

class DoctorAvailabilityInline(admin.TabularInline):
    model = DoctorAvailability
    extra = 0

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'experience_years', 'is_active', 'available_days')
    inlines = [DoctorAvailabilityInline]

    # Custom column to show available days as a comma-separated list
    def available_days(self, obj):
        # Get all days where is_active is True (available days)
        days = obj.doctoravailability_set.filter(is_active=True)
        return ", ".join([d.get_day_of_week_display() for d in days])

    available_days.short_description = "Available Days"  # Name of the column

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'experience_years', 'is_active', 'available_days')
    inlines = [DoctorAvailabilityInline]

    # Custom method to handle available days as comma-separated
    def available_days(self, obj):
        days = obj.doctoravailability_set.filter(is_active=True)
        return ", ".join([d.get_day_of_week_display() for d in days])

    available_days.short_description = "Available Days"

    # Action to deactivate a doctor
    def deactivate_doctor(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, "Selected doctors have been deactivated.")

    # Custom action in the admin panel for batch deactivation
    deactivate_doctor.short_description = "Deactivate Selected Doctors"

    actions = [deactivate_doctor]

# Registering the Doctor model with the custom admin class


# Registering the Doctor model with the custom admin class
admin.site.register(Doctor, DoctorAdmin)
