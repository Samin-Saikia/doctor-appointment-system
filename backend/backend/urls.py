
from django.contrib import admin
from django.urls import path, include
from .views import api_home
urlpatterns = [
    path('', api_home),
    path('admin/', admin.site.urls),
    path('api/', include('doctors.urls')),
    path('api/', include('appointments.urls')),
    path('api/', include('departments.urls')),
    path('api/', include('payments.urls')),
    path('api/', include('auth_app.urls')),
    
]




