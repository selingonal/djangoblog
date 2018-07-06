#imports
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Comment
from accounts.models import User
from .forms import PostForm, CommentForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.conf import settings


#please refer to post_create's comments as a reference for repetitive code

def post_create(request): #Create
	#Permissons to create a post are limited to staff, superusers, and users with author authorization
	if not request.user.is_authenticated:
		raise PermissionDenied

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.user = request.user
		instance.save()
		form=PostForm()
		messages.success(request, "Successfully Created!")
		return HttpResponseRedirect('/posts/')
	context={
		"form": form,
	}
	'''
	returns the request the function makes to the html file "post_form.html"
	(request // hmtl file-- located in templates // context)
	context is a dictionary with variable names as the "key" and their values as the "value"
	here
	'''
	return render(request, "post_form.html",context)


def post_detail(request, id=None): #retrieve
	
	if not request.user.is_authenticated:
		raise PermissionDenied

	#calls the post's individual id
	instance = get_object_or_404(Post, id=id)
	#this displays comments under the indivual post
	comments= Comment.objects.filter(post = id)

	context ={
		"title": instance.title,
		"instance": instance,
		"comments":comments,
	}
	return render(request, "post_detail.html",context)


def post_list(request): #list items

	if not request.user.is_authenticated:
		raise PermissionDenied

	#Search Query code
	query= request.GET.get('q')
	if query:
		queryset_list=Post.objects.filter(Q(title__icontains=str(query))| Q(content__icontains=str(query)))
	# calls to display all objects now in the event that there is no query
	else:
		queryset_list= Post.objects.all()
	'''
	Paginator is what separates posts into separate 
	pages rather than having one really long list
	'''
	paginator = Paginator(queryset_list, 10) # Show 10 contacts per page
	#adds on the the paginator, renders the page we requested
	page = request.GET.get('page')
	queryset = paginator.get_page(page)

	context ={
			"object_list" : queryset,
			"title": "List"
		}
	return render(request, "post_list.html",context)
'''
 #I don't quite remember what this is or what it does 
def listing(request):
    contact_list = Contacts.objects.all()
    return render(request, 'post_list.html', {'queryset': queryset_list})
'''

def post_update(request, id =None): #edit
	if request.user.is_authenticated and request.user == Post.user:	
		
		instance = get_object_or_404(Post, id=id)
		
		form = PostForm(request.POST or None, request.FILES or None, instance =instance)
		#to edit, we're reopening the form we used to create the post and updating accordingly
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			messages.success(request, "Item Saved!")
			form=PostForm()
			return HttpResponseRedirect(instance.get_absolute_url())
		context={
			"form": form,
		}
		return render(request, "post_form.html", context)
		
	else:
		raise PermissionDenied


def post_delete(request, id=None): #delete
	if not request.user.is_authenticated:
		raise PermissionDenied
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance =instance)
	#django already gives us a function to delete, so that's what we're using
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	context ={
		"form":form,
	}
	return HttpResponseRedirect('/posts/')


def add_comment(request, id=None):
	if not request.user.is_authenticated:
		raise PermissionDenied
	post= get_object_or_404(Post, id=id)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.user = request.user
			comment.save()
			return HttpResponseRedirect(post.get_absolute_url())
	else:
		form = CommentForm()

	context = {
		'form':form
		}
	return render(request,'add_comment.html', context)
'''

def view_comment(request,pk=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise PermissionDenied
	instance = get_object_or_404(Post, pk=pk)
	context ={
		"title": instance.title,
		"instance": instance,
		"comments":comments,
	}
	return render(request, "post_detail.html",context)


def comment_update(request, pk=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise PermissionDenied
	post= get_object_or_404(Comment, pk=pk)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return HttpResponseRedirect(post.get_absolute_url())
	else:
		form = CommentForm()

	context = {
		'form':form
		}
	return render(request,'add_comment.html', context)

def comment_delete(request, pk=None):
	if not request.user.is_staff or not request.user.is_superuser or not request.user.post.author:
		raise PermissionDenied
	instance = get_object_or_404(Comment, pk=pk)
	form = CommentForm(request.POST or None, instance =instance)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	context ={
		"form":form,
	}
	return HttpResponseRedirect(post.get_absolute_url())
'''
