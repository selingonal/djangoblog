from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
# The method we are designing, this app around is CRUD
# CREATE -- MAKE NEW
# RETRIEVE -- GET
# UPDATE -- EDIT
# DELETE -- DELETE

def post_create(request): #Create
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		form=PostForm()
		messages.success(request, "Successfully Created!")
		return HttpResponseRedirect('/posts/')
	context={
		"form": form,
	}
	return render(request, "post_form.html",context)


def post_detail(request, id=None): #retrieve
	instance = get_object_or_404(Post, id=id)
	context ={
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html",context)


def post_list(request): #list items
	queryset= Post.objects.all()
	context ={
			"object_list" : queryset,
			"title": "List"
		}
	return render(request, "index.html",context)


def post_update(request, id =None): #edit
	
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance =instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		messages.success(request, "Item Saved!")
		form=PostForm()
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
		# "title": instance.title,
		# "instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)


def post_delete(request, id=None): #delete
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance =instance)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	context ={
		"form":form,
	}
	return HttpResponseRedirect('/posts/')
























