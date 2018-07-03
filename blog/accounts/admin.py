from django.contrib import admin

# Register your models here.
from .models import User

class Users(admin.ModelAdmin):
	class Meta:
		model = User

admin.site.register(User)
