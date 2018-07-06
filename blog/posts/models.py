from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.
# MVC == model view controller


def upload_location(instance, filename):
	return "%s/%s" %(instance.id,filename)

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE)
	# if you don't have a max length for your char field, it won't migrate. 
	title = models.CharField(max_length=120) 
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	#file = models.FileField(null=True, blank = True)
	image = models.ImageField(upload_to=upload_location,
			null=True,
			blank = True,
			width_field="width_field",
			height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)


	#use __str__ specifically for python 3
	def __str__ (self):
		return self.title

	def get_absolute_url(self):
		return reverse("detail", kwargs={"id":self.id})
		#return "/posts/%s" %(self.id)

	class Meta:
		ordering = ["-updated","-timestamp"]

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=False, blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	user = models.CharField(max_length=250)
	content = models.TextField()
	image = models.ImageField(
		upload_to=upload_location,
		null=True,
		blank = True,
		width_field="width_field",
		height_field="height_field")
	approved = models.BooleanField(default=False)

	def approved(self):
		self.approved = True
		self.save()

	def __str__ (self):
		return self.user
	def get_absolute_url(self):
		return reverse("detail", kwargs={"id":self.id})











