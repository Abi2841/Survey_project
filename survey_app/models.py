from django.db import models

# Create your models here.
# models.py
from django.db import models

class ElectionSurveyDetails(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
    )
    dob = models.DateField()
    city = models.CharField(max_length=50)
    PARTY_CHOICES = [
        ('AAA', 'AAA'),
        ('AAB', 'AAB'),
        ('AAC', 'AAC'),
        ('AAD', 'AAD'),
    ]
    party_name = models.CharField(
        max_length=3,
        choices=PARTY_CHOICES,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name