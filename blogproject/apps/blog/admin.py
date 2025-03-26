from django.contrib import admin
from apps.blog.models import BlogPost
# Register your models here.

@admin.register(BlogPost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title','author','image','created_at')
    search_fields = ('title','content')
    prepopulated_fields = {'slug':('title',)}