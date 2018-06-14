from django.contrib import admin
# it is "." models because they are in teh same directory
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp", "title"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
	list_display = ["user", "timestamp", "approved"]
	class Meta:
		model = Comment

admin.site.register(Comment, CommentAdmin)
