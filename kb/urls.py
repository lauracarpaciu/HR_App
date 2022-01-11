
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='kb-home'),
    path('about/', views.about, name='kb-about'),
    path('article/new/', views.ArticleCreateView.as_view(), name = 'new-article'),

]