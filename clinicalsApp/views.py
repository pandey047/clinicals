from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from clinicalsApp.models import Patient
from clinicalsApp.forms import ClinicalsDataForm
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
# Create your views here.
class PatientListView(ListView):
     model=Patient

class PatientCreateview(CreateView):
    model=Patient
    fields=('firstName','lastName','age')
    success_url=reverse_lazy('index')

class PatientUpdateView(UpdateView):
    model=Patient
    fields=('firstName','lastName','age')
    success_url=reverse_lazy('index')

class PatientDeleteView(DeleteView):
    model=Patient
    success_url=reverse_lazy('index')


def addData(request,**kwargs):
    form=ClinicalsDataForm()
    patient=Patient.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form=ClinicalsDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalsApp/clinicalsdata_form.html',{'form':form,'patient':patient})
