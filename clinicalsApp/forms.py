from django import forms
from clinicalsApp.models import Patient,ClinicalsData
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'

class ClinicalsDataForm(forms.ModelForm):
    class Meta:
        model=ClinicalsData
        fields='__all__'
