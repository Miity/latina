from django.contrib import admin
from .models import Post
# Register your models here.



class PostAdmin(admin.ModelAdmin):
	fieldsets = (
		('На странице блога', {
			'fields': ('post_photo',)
			}),
		("Пост:", {
			'fields': ('post_author','post_title','post_text','post_date')
			})
		)

admin.site.register(Post, PostAdmin)