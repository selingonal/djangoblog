from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

#this is an example of a function based view
# CRUD
# CREATE -- MAKE NEW
# RETRIEVE -- GET
# UPDATE -- EDIT
# DELETE -- DELETE

def post_create(request): #Create
	return HttpResponse("<h1> Create</h1>")
def post_detail(request): #retrieve
	context ={
		"title": "Detail"
		
	}
	return render(request, "index.html",context)
	#return HttpResponse("<h1> Detail</h1>")
def post_list(request): #list items
	queryset= Post.objects.all()
	context ={
			"object_list" : queryset,
			"title": "My User List"
		}
	# if request.user.is_authenticated():
	# 	context ={
	# 		"object_list":queryset
	# 		"title": "My User List"
	# 	}
	# else: 
	# 	context ={
	# 		"title": "List"
	# 	}
	return render(request, "index.html",context)
def post_update(request): #edit
	return HttpResponse("<h1> Update</h1>")
def post_delete(request): #delete
	return HttpResponse("<h1> Delete</h1>")
