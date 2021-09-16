from django.db import models

# Create your models here.
class Patient(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
        return self.firstName

class ClinicalsData(models.Model):
    COMPONENT_NAME=[('Heart Rate','Heart Rate'),('BP','Blood Pressure'),('Sugar','Sugar')]
    componentName=models.CharField(choices=COMPONENT_NAME,max_length=20)
    componentValue=models.CharField(max_length=20)
    measureDateTime=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
