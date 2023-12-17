from django.contrib import admin
from .models import Patient, TestOrder, Test

admin.site.register(Patient)
admin.site.register(TestOrder)
admin.site.register(Test)

# Register your models here.
