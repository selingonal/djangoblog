from django.http import HttpResponse
from django.shortcuts import render

#this is an example of a function based view
# CRUD
# CREATE -- MAKE NEW
# RETRIEVE -- GET
# UPDATE -- EDIT
# DELETE -- DELETE

def post_create(request): #Create
	return HttpResponse("<h1> Create</h1>")
def post_detail(request): #retrieve
	return HttpResponse("<h1> Detail</h1>")
def post_list(request): #list items
	return HttpResponse("<h1> List</h1>")
def post_update(request): #edit
	return HttpResponse("<h1> Update</h1>")
def post_delete(request): #delete
	return HttpResponse("<h1> Delete</h1>")
