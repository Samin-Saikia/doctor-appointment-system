from django.contrib import admin
from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'fee', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)

admin.site.register(Department, DepartmentAdmin)
