from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('posts/', views.posts, name="Posts"),
    path('posts/<slug:slug>/', views.post_detail, name="Post_Detail")
]
