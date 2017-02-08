from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comments
from .forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
# Create your views here.

def main(request):
    return render(request, 'index.html', {'user_name': auth.get_user(request).username})

def blog(request, page_number = 1):
    posts_list = Post.objects.all()
    current_page = Paginator(posts_list, 2)
    return render(request, 'blog.html', {'posts': current_page.page(page_number), 'user_name': auth.get_user(request).username})

def post_detail(request, pk):
    args = {}
    args.update(csrf(request))
    args['post'] = get_object_or_404(Post, pk=pk)
    args['comments'] = Comments.objects.filter(comments_post_id = pk)
    args['form'] = CommentForm
    args['user_name'] = auth.get_user(request).username
    return render(request, 'post_detail.html', args)

def addcomment(request, pk):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_post = Post.objects.get(id=pk)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/blog/post/{}/'.format(pk))