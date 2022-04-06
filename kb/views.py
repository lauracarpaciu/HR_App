from datetime import timezone
from .models import Countrie, Department, Employee, Job_History, Job, Location, Region
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.contrib.staticfiles.views import serve
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
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


def search(request):
    template='kb/home.html'
    query=request.GET.get('q')
    result=Employee.objects.filter(Q(last_name__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query)| Q(first_name__icontains=query))
    paginate_by=2
    context={ 'employees_list':result }
    return render(request,template,context)


def about(request):
    # return HttpResponse('<h1> About knowledge base</h1>')
    context = {'title': 'About KB'}
    return render(request, 'kb/about.html', context)

def getfile(request):
   return serve(request, 'File')


class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees_list'
    template_name = 'kb/home.html'  
    ordering = ['-date_posted']
    paginate_by = 2

class UserEmployeeListView(ListView):
    model = Employee
    template_name = 'kb/user_posts.html' 
    context_object_name = 'employees_list'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return Employee.objects.filter(author=user).order_by('-date_posted')

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'kb/post_detail.html'
    context_object_name = 'employees_list'
    queryset = Employee.objects.all()
    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.utc
        obj.save()
        return obj

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    fields = '__all__' # fields
    success_url = reverse_lazy('post-create')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EmployeeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Employee
    fields = '__all__' # fields
    success_url = reverse_lazy('kb-home')
    template_name = 'kb/update_form.html' # templete for updating

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 
class EmployeeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Employee
    template_name = 'kb/post_confirm_delete.html'
    success_url = reverse_lazy('kb-home')
    
    def form_valid(self, form):
        form.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False       

from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.

def generatePDF(request, id):
    buffer = io.BytesIO()
    x = canvas.Canvas(buffer)
    x.drawString(100, 100, "Let's generate this pdf file.")
    x.showPage()
    x.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='attempt1.pdf')





