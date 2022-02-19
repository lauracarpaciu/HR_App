
from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    UserArticleListView
)


from . import views

urlpatterns = [
    path('', views.home, name='kb-home'),
    path('about/', views.about, name='kb-about'),
    path('', ArticleListView.as_view(), name='kb-home'),
    path('user/<str:username>', UserArticleListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', ArticleDetailView.as_view(), name='post-detail'),
    path('post/new/', ArticleCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', ArticleUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', ArticleDeleteView.as_view(), name='post-delete'),
    path('media/Files/<int:pk>',ArticleDeleteView.as_view(),name='post-delete' ),
    path('search/',views.search,name='search' ),
  
]