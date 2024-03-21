from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('register/', views.register_view, name='register'),

    # Separate registration URLs for doctor and patient (optional, based on your design)
    path('doctor/register/', views.doctor_register, name='doctor_register'),
    path('patient/register/', views.patient_register, name='patient_register'),

    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),

    # Blog management URLs (optional, for doctors)
    path('create_blog/', views.create_blog, name='create_blog'),
    path('edit_blog/<int:pk>/', views.edit_blog, name='edit_blog'),  # Dynamic URL for editing specific blog
    # path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),  # Dynamic URL for viewing specific blog
]
