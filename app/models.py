from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
# Create your models here.
INCIDENT_CHOICES = (('CH', 'Coporate Headoffice'),('OD', 'Operation Depratment'),('WS', 'Work Station'),('MD', 'Marketing Division'),)
SEVERITY_CHOICES = (('M', 'Mild'),('MO', 'Moderate'),('S', 'Severe'),('F', 'Fatal'),)
INCIDENT_TYPES = (('E', 'Environmental incident'),('I', 'Injury'),('P', 'Property damage'),('V', 'Vehicle'),('O', 'Other'))

class Report_info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    location = models.CharField(choices=INCIDENT_CHOICES, max_length=2)
    incident_department = models.TextField(max_length=255)
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(auto_now_add=True)
    incident_location = models.TextField(max_length=255, blank=True, null=True)
    initial_severity = models.CharField(choices=SEVERITY_CHOICES, max_length=2)
    suspected_cause = models.TextField(max_length=255)
    action_taken = models.TextField(max_length=255)
    incident_types = models.CharField(choices=INCIDENT_TYPES, max_length=2)

    def __str__(self):
        return str(self.user) 