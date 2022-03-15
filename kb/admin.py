from django.contrib import admin
from .models import Region
from .models import Countrie
from .models import Location
from .models import Department
from .models import Job
from .models import Employee
from .models import Job_History

class JobInline(admin.TabularInline):
    model = Job
    extra = 3

class EmployeeAdmin(admin.ModelAdmin):
    fields = '__all__'
    inlines = [JobInline]

# Register your models here.
admin.site.register(Region)
admin.site.register(Countrie)
admin.site.register(Location)
admin.site.register(Department)
admin.site.register(Job)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Job_History)

