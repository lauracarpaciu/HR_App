from django.db import models
from django.utils import timezone
# Create your models here.

class Regions(models.Model):
    region_name = models.CharField(max_length=25)

    def __str__(self):
        return self.region_name
    class Meta:
        ordering = ['region_name']


class Countries(models.Model):
    country_name = models.CharField(max_length=40,default='DEFAULT VALUE')
    regions = models.ForeignKey(Regions, on_delete=models.CASCADE)

    def __str__(self):
        return self.country_name

    class Meta:
        ordering = ['country_name']


class Locations(models.Model):
    street_address = models.CharField(max_length=25)
    postal_code = models.CharField(max_length=12)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=12)
    countries = models.ForeignKey(Countries, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.street_address

    class Meta:
        ordering = ['street_address']

class Departments(models.Model):
    depart_name = models.CharField(max_length=30,default='DEFAULT VALUE')
    locations = models.ForeignKey(Locations,on_delete=models.CASCADE)

    def __str__(self):
        return self.depart_name

    class Meta:
        ordering = ['depart_name']      

class Jobs(models.Model):
    job_title = models.CharField(max_length=35)
    min_salaty = models.IntegerField()
    max_salary = models.IntegerField()
    
    def __str__(self):
        return self.job_title

    class Meta:
        ordering = ['job_title'] 

class Employees(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    hire_date = models.DateField()
    salary = models.IntegerField()
    commission_pct = models.IntegerField()
    departments = models.ForeignKey(Departments,on_delete=models.CASCADE)
    jobs = models.ForeignKey(Jobs,on_delete=models.CASCADE)

def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)       
    

class Job_History(models.Model):
    jobs = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    departments = models.ForeignKey(Departments,on_delete=models.CASCADE)
    employees = models.ForeignKey(Employees,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.start_date

    class Meta:
        ordering = ['start_date']   

