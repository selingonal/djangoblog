from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
from .forms import UserLoginForm, UserRegisterForm
from django.shortcuts import render, redirect

def login_view(request):
	title = "Login"
	form=UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		login(request, user)
		return redirect("/posts")
	return render(request, "forms.html", {"form":form},{"title":title})


def register_view(request):
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user=form.save(commit=False)
		password=form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username = user.username, password=user.password, is_staff=True)
		
		login(request,user)
		return redirect("/login")

	context = {
		"form":form,
		"title":title,
	}
	return render(request, "forms.html", context)

def logout_view(request):
	logout(request)
	return render(request, "logout.html", {})

def default_home(request):
	return render(request, "home.html",{})