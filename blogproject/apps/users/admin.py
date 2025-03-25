from django.contrib import admin

# Register your models here.
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','email','role','is_staff')
    list_filter = ('role','is_staff')
    search_fields = ('username','email')
    actions = ['make_auhor']

    def make_author(self,request,queryset):
        queryset.update(role='author')
    make_author.short_description = "Mark selected users as Authors"

admin.site.register(CustomUser)