from django.contrib import admin
from .models import Post, Comments
# Register your models here.


class PostInline(admin.StackedInline):
	model = Comments
	extra = 2


class PostAdmin(admin.ModelAdmin):
	fieldsets = (
		('На странице блога', {
			'fields': ('post_photo',)
			}),
		("Пост:", {
			'fields': ('post_author','post_title','post_text','post_date')
			})
		)
	inlines = [PostInline]

admin.site.register(Post, PostAdmin)