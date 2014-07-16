from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from posts.models import Post
from forms import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'templates/index.html', {'posts': posts})

def new(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        return HttpResponseRedirect('/posts/')
    
    return render_to_response("templates/create.html",locals(),context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/posts/")