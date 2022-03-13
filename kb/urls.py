
from django.urls import path

from .views import (
    EmployeeListView,
    EmployeeDetailView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    UserEmployeeListView
)


from . import views

urlpatterns = [

    path('', EmployeeListView.as_view(), name='kb-home'),
    path('user/<str:username>', UserEmployeeListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', EmployeeDetailView.as_view(), name='post-detail'),
    path('post/add/', EmployeeCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', EmployeeUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='post-delete'),
    path('media/Files/<int:pk>',EmployeeDeleteView.as_view(),name='post-delete' ),
    path('search/',views.search,name='search' ),
    path('about/', views.about, name='kb-about'),
    ]