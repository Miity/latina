from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comments, Category
from django.contrib import auth
from .forms import CommentForm
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


# страница блога (всех статтей)
def blog(request, category_slug=None,):
    category = None
    categories = Category.objects.all()
    post = Post.objects.filter(post_available=True)
    current_page = Paginator(post, 5)
    page = request.GET.get('page')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = Post.objects.filter(post_category=category)
        current_page = Paginator(post, 2)
        page = request.GET.get('page')

    try:
        posts = current_page.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = current_page.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = current_page.page(current_page.num_pages)

    return render(request, 'blog.html', {
        'category': category,
        'categories': categories,
        'posts': posts
    })


# Страница поста
def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, post_slug=slug, post_available=True)
    return render(request, 'post_detail.html', {'post': post})


def addcomment(request, id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_user = request.user
            comment.comments_post = Post.objects.get(id=id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/blog/post/{}/'.format(id))