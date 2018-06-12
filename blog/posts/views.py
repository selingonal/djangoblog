from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

# The method we are designing, this app around is CRUD
# CREATE -- MAKE NEW
# RETRIEVE -- GET
# UPDATE -- EDIT
# DELETE -- DELETE

def post_create(request): #Create
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	if not request.useris_authenticated():
		raise Http404

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
		raise Http404
	instance = get_object_or_404(Post, id=id)
	context ={
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html",context)


def post_list(request): #list items
	queryset_list= Post.objects.all()
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page

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
		raise Http404
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
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance =instance)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	context ={
		"form":form,
	}
	return HttpResponseRedirect('/posts/')
























