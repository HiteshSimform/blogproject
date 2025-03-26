from django.urls import path
from apps.blog.views import blog_list, blog_details, create_post, edit_post, delete_post

urlpatterns = [
    path('',blog_list,name='blog_list'),
    # path('details/<slug:slug>/<str:name>/',blog_details,name='blog_details'),
    path('details/<slug:slug>/',blog_details,name='blog_details'),
    path('create/',create_post,name='create_post'),
    path('edit/<slug:slug>',edit_post,name='edit_post'),
    path('delete/<slug:slug>',delete_post,name='delete_post'),
]   