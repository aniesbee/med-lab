from django.shortcuts import render
from django.views.generic import ListView

from .models import Patient, TestOrder, Test

class PatientListView(ListView):
    model = Patient

# Create your views here.
