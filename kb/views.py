from django.shortcuts import render
from .models import Countrie, Department, Employee, Job_History, Job, Location, Region
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    regions_list = Region.objects.all()
    countries_list = Countrie.objects.all()
    locations_list = Location.objects.all()
    departments_list = Department.objects.all()
    employees_list = Employee.objects.all()
    jobs_list = Job.objects.all()
    job_history_list = Job_History
    
    context = {
        'title': 'Articles',
        'regions_list': regions_list,
        'countries_list': countries_list,
        'locations_list': locations_list,
        'departments_list': departments_list,
        'employees_list': employees_list,
        'jobs_list': jobs_list,
        'job_history_list': job_history_list
    }
    
    return render(request, 'kb/home.html', context)



def about(request):
    # return HttpResponse('<h1> About knowledge base</h1>')
    context = {'title': 'About KB'}
    return render(request, 'kb/about.html', context)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Region
    fields = ['region_name']
    success_url = reverse_lazy('kb-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)