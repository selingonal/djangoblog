from django.db import models

# Create your models here.
# MVC == model view controller
class Post(models.Model):
	# if you don't have a max length for your char field, it won't migrate. 
	title = models.CharField(max_length=120) 
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	#use __str__ specifically for python 3
	def __str__ (self):
		return self.title