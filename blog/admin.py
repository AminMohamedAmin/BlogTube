from django.contrib import admin
from .models import Post, Post_Like, Post_Comment

# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","update","puplish"]
	list_filter = ["puplish","title"]
	search_fields = ["title","content"]
	class Meta:
		model = Post


admin.site.register(Post,PostModelAdmin)


class PostLikeModelAdmin(admin.ModelAdmin):
	list_display = ["post","user"]
	list_filter = ["post"]
	search_fields = ["post"]
	class Meta:
		model = Post_Like


admin.site.register(Post_Like,PostLikeModelAdmin)


class PostCommentModelAdmin(admin.ModelAdmin):
	list_display = ["post","user","comment"]
	list_filter = ["post"]
	search_fields = ["post"]
	class Meta:
		model = Post_Comment


admin.site.register(Post_Comment,PostCommentModelAdmin)