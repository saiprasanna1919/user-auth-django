from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import Truncator


class User(AbstractUser):
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    address_line1 = models.CharField(max_length=255, blank=True)  # Optional address fields
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=15, blank=True)
    confirm_password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

CATEGORY_CHOICES = (
    ('mental_health', 'Mental Health'),
    ('heart_disease', 'Heart Disease'),
    ('covid19', 'Covid19'),
    ('immunization', 'Immunization'),
)



class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/', blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    summary = models.TextField(max_length=255)
    content = models.TextField()
    is_draft = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')

    def get_truncated_summary(self):
        return Truncator(self.summary).chars(15) + "..." if len(self.summary) > 15 else self.summary