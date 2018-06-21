#imports#
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.core.exceptions import PermissionDenied



def post_create(request): #Create
	if not request.user.is_staff or not request.user.is_superuser:
		raise PermissionDenied
	# if not request.useris_authenticated():
	# 	raise PermissionDenied

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
	return render(request, "post_form.html",context)


def post_detail(request, id=None): #retrieve
	if not request.user.is_staff or not request.user.is_superuser:
		raise PermissionDenied
	instance = get_object_or_404(Post, id=id)
	comments= Comment.objects.filter(post = id)

	context ={
		"title": instance.title,
		"instance": instance,
		"comments":comments,
	}
	return render(request, "post_detail.html",context)


def post_list(request): #list items
	queryset_list= Post.objects.all()
	paginator = Paginator(queryset_list, 10) # Show 10 contacts per page
	#search query
	query= request.GET.get('q')
	if query:
		 queryset_list=queryset_list.filter(title__icontains=query)
	page = request.GET.get('page')
	queryset = paginator.get_page(page)

	context ={
			"object_list" : queryset,
			"title": "List"
		}
	return render(request, "post_list.html",context)

def listing(request):
    contact_list = Contacts.objects.all()
    return render(request, 'list.html', {'queryset': queryset_list})


def post_update(request, id =None): #edit
	if not request.user.is_staff or not request.user.is_superuser:
		raise PermissionDenied
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance =instance)
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
	if not request.user.is_staff or not request.user.is_superuser or not request.user.post.author:
		raise PermissionDenied
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance =instance)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	context ={
		"form":form,
	}
	return HttpResponseRedirect('/posts/')

def add_comment(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise PermissionDenied
	post= get_object_or_404(Post, id=id)
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


def comment_update(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise PermissionDenied
	post= get_object_or_404(Post, id=id)
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

def comment_delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise PermissionDenied
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance =instance)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	context ={
		"form":form,
	}
	if not request.user.is_superuser or not request.user.is_valid:
		raise Http404
	else:
		return HttpResponseRedirect(post.get_absolute_url())


