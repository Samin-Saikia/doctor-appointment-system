from django.http import HttpResponse

def api_home(request):
    return HttpResponse("""
    <h1>Doctor Appointment Booking API</h1>
    <p>This is a backend-only REST API project built with Django.</p>

    <h3>Available Endpoints:</h3>
    <ul>
        <li><b>Admin Panel:</b> <a href="/admin/">/admin/</a></li>
        <li><b>Doctors API:</b> /api/doctors/</li>
        <li><b>Appointments API:</b> /api/appointments/</li>
        <li><b>Departments API:</b> /api/departments/</li>
        <li><b>Payments API:</b> /api/payments/</li>
        <li><b>Authentication API:</b> /api/users/</li>
    </ul>

    <p>Use Postman or any REST client to interact with the APIs.</p>
    """)
