from django.urls import path
from django.contrib import admin
from . import views

urlpatterns =[
    path(r'', views.post_list),
    path(r'create/', views.post_create),
    path(r'detail/', views.post_detail),
    path(r'update/', views.post_update),
    path(r'delete/', views.post_delete),


]