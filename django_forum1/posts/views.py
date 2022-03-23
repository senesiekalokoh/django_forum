from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from cloudinary.forms import cl_init_js_callbacks
from django.urls import reverse_lazy, reverse

def index(request):
    # If the message is POST
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())


    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    # Show
    return render(request, 'posts.html',
                  {'posts': posts})

def delete(request, post_id):
    # Find Post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')
def like(request, post_id):
    post = Post.objects.get(id=post_id)
    new_like_count = post.like_count + 1
    post.like_count = int(new_like_count)
    post.save()
    return HttpResponseRedirect('/')
    
def update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else: 
        form=PostForm
        return render(request, 'update.html', {'post':post, 'form':form})