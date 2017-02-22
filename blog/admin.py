from django.contrib import admin
from .models import Post, Comments, Category


# Register your models here.

# дополнение к комментариям
class PostInline(admin.StackedInline):
    model = Comments
    extra = 1


# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


# Модель поста
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title','post_created','post_updated','bit','post_available',]
    list_filter = ['post_available', 'post_created', "post_updated"]
    list_editable = ['post_available']
    inlines = [PostInline]
    search_fields = ['post_title']
    prepopulated_fields = {'post_slug': ('post_title',)}


# Регистрация моделей
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
