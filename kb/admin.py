from django.contrib import admin
from .models import Reporter
from .models import Article

# Register your models here.
admin.site.register(Reporter)
admin.site.register(Article)