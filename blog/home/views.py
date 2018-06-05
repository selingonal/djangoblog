from django.shortcuts import HttpResponse
from django.template import loader
from home.models import Home

def index(request):
    home_page = Home.objects.all()
    template = loader.get_template("home/index.html")
    context = {
        'home': home_page,
    }
    return HttpResponse(template.render(context, request))

    #html = "<h1> THIS IS THE TEMPORARY HOMEPAGE</h1>" 
   # return HttpResponse(html)
