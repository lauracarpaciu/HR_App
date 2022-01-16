from django.contrib import admin
from .models import Regions
from .models import Countries
from .models import Locations
from .models import Departments
from .models import Jobs
from .models import Employees
from .models import Job_History

# Register your models here.
admin.site.register(Regions)
admin.site.register(Countries)
admin.site.register(Locations)
admin.site.register(Departments)
admin.site.register(Jobs)
admin.site.register(Employees)
admin.site.register(Job_History)

