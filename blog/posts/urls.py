from django.urls import path, re_path
from django.contrib import admin
from . import views

urlpatterns =[
    path(r'', views.post_list),
    path(r'create/', views.post_create),
    re_path(r'(?P<id>\d+)/edit/$', views.post_update, name = 'update'),
    re_path(r'(?P<id>\d+)/', views.post_detail, name='detail'),
    path(r'delete/', views.post_delete),
]

