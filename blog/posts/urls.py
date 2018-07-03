from django.urls import path, re_path
from django.contrib import admin
from . import views

from .views import(
	post_list,
	post_detail,
	post_create,
	post_update,
	post_delete,
	add_comment,
	#comment_update,
	#comment_delete,
	#view_comment,
	)
urlpatterns =[
    path(r'', post_list, name='list'),
    path(r'create/', post_create),
    re_path(r'(?P<id>\d+)/comment', add_comment, name='add_comment'),
    re_path(r'(?P<id>\d+)/comment/(?P<pk>\d+)/', add_comment, name='add_comment'),
    #re_path(r'(?P<id>\d+)/comment/(?P<pk>\d+)/', view_comment, name='view_comment'),
    re_path(r'(?P<id>\d+)/edit/$', post_update, name = 'update'),
    re_path(r'(?P<id>\d+)/delete/$', post_delete),
    # re_path(r'?P<id>\d+)/comment/(?P<pk>\d+)/comdelete/$', 'comment_delete'),
    # re_path(r'?P<id>\d+)/comment/(?P<pk>\d+)/comedit/$', 'comment_update'),
    re_path(r'(?P<id>\d+)/', post_detail, name='detail'),
]

