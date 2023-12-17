from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50, choices=(('male', 'Male'), ('female', 'Female')))
    age = models.IntegerField()
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return self.name

class TestOrder(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='test_orders')
  test_order_desc = models.CharField(max_length=100)
  clinic = models.CharField(max_length=50)
  doctor = models.CharField(max_length=50)
  staus = models.CharField(max_length=50, choices=(('pending', 'Pending'), ('completed', 'Completed')))
  test_date = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.test_order_desc

class Test(models.Model):
  test_order = models.ForeignKey(TestOrder, on_delete=models.CASCADE, related_name='tests')
  name = models.CharField(max_length=50)
  specimen = models.CharField(max_length=50)
  result = models.TextField()
  def __str__(self):
    return self.name


  
  






# Create your models here.
