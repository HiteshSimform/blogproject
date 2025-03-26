from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.blog.models import BlogPost
from apps.blog.forms import BlogPostForm
from django.http import Http404
from django.urls import reverse
from apps.blog import signals
# Create your views here.

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html',{'posts':posts})

def blog_details(request,slug):
    try:
        post = get_list_or_404(BlogPost, slug=slug)[0]
    except Http404:
        return render(request, 'blog/404Error.html')
    return render(request, 'blog/blog_detail.html', {'post': post})

# def blog_details(request,slug,name):
#     try:
#         post = get_list_or_404(BlogPost, slug=slug)[0]
#     except Http404:
#         return render(request, 'blog/404Error.html')
#     return render(request, 'blog/blog_detail.html', {'post': post})
@login_required(login_url='login-user')
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request,"Post created successfully")
            signals.email_signal.send(sender=None, subject="Hello",message="Hi",to_email="artistkarm2211@gmail.com")
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request,'blog/create_post.html',{'form':form})

def edit_post(request,slug):
    # post = get_list_or_404(BlogPost,slug = slug, author = request.user)[0]
    # print(request.user)
    post = get_list_or_404(BlogPost,slug = slug, author = request.user)[0]
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES, instance = post)
        if form.is_valid():
            form.save()
            messages.success(request,"Post Updated Successfully")
            return redirect(reverse('blog_details',kwargs={'slug':slug}))
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/edit_post.html',{'form':form})


# def edit_post(request,slug):
#     # post = get_list_or_404(BlogPost,slug = slug, author = request.user)[0]
#     post = get_list_or_404(BlogPost,slug = slug, author = request.user)[0]
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST,request.FILES, instance = post)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Post Updated Successfully")
#             return redirect(reverse('blog_details',kwargs={'slug':slug,'name':"hitesh"}))
#     else:
#         form = BlogPostForm(instance=post)
#     return render(request, 'blog/edit_post.html',{'form':form})

def delete_post(request,slug):
    post = BlogPost.objects.get(slug=slug)
    post.delete()

    messages.success(request,"Deleted Successfully")
    return redirect(reverse('blog_list'))

