from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import DoctorRegistrationForm, PatientRegistrationForm, BlogCreationForm
from .models import Blog

def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('doctor_dashboard')  # Redirect to doctor dashboard
    else:
        form = DoctorRegistrationForm()
    return render(request, 'user_management/doctor_register.html', {'form': form})

def patient_register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient_dashboard')  # Redirect to patient dashboard
    else:
        form = PatientRegistrationForm()
    return render(request, 'user_management/patient_register.html', {'form': form})


def doctor_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'doctor':
        return redirect('login')  # Redirect to login if not a doctor

    user_blogs = Blog.objects.filter(author=request.user)  # Filter blogs by logged-in doctor
    return render(request, 'user_management/doctor_dashboard.html', {'blogs': user_blogs})


def create_blog(request):
    if not request.user.is_authenticated or request.user.role != 'doctor':
        return redirect('login')  # Redirect to login if not a doctor

    if request.method == 'POST':
        form = BlogCreationForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)  # Don't save yet as we need to set the author
            blog.author = request.user
            blog.save()
            return redirect('doctor_dashboard')
    else:
        form = BlogCreationForm()
    return render(request, 'user_management/create_blog.html', {'form': form})

def patient_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'patient':
        return redirect('login')  # Redirect to login if not a patient

    published_blogs = Blog.objects.filter(is_draft=False)  # Get published blogs
    return render(request, 'user_management/patient_dashboard.html', {'blogs': published_blogs})


def login_view(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'doctor':
                return redirect('doctor_dashboard')
            elif user.role == 'patient':
                return redirect('patient_dashboard')
        else:
            # Handle invalid credentials
            pass  # Implement error handling for invalid login
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def edit_blog(request, pk):
    pass