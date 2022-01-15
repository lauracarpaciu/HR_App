from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100,default='DEFAULT VALUE')
    pub_date = models.DateField(default=timezone.now)
    reporter = models.ForeignKey(Reporter,default='DEFAULT VALUE', on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']