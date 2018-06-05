from django.http import HttpResponse
from django.template import loader
from users.models import User

def index(request):
    all_users = User.objects.all()
    template = loader.get_template("users/index.html")
    context = {
        'all_user': all_users,
    }
    return HttpResponse(template.render(context, request))

    #html = "<h1> This is where the users will be displayed</h1>" 
    #return HttpResponse(html)

