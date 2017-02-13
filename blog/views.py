from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comments, Category
from .forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
# Create your views here.

def main(request):
    return render(request, 'index.html', {'user_name': auth.get_user(request).username})

# страница блога (всех статтей)
def blog(request, category_slug=None, page_number = 1):
    category = None
    categories = Category.objects.all()
    post = Post.objects.filter(post_available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = Post.objects.filter(post_category=category)
    return render(request, 'blog.html', {
        'category': category,
        'categories': categories,
        'posts': post
    })

    '''
    def blog(request, page_number = 1):
    posts_list = Post.objects.all()
    current_page = Paginator(posts_list, 6)
    return render(request, 'blog.html', {'posts': current_page.page(page_number),
                                        'nodes':Category.objects.all(),'user_name': auth.get_user(request).username})
    '''

# Страница поста
def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, post_slug=slug, post_available=True)
    return render(request, 'post_detail.html', {'post': post})

    '''
    args = {}
    args.update(csrf(request))
    args['post'] = get_object_or_404(Post, pk=pk)
    args['comments'] = Comments.objects.filter(comments_post_id = pk)
    args['form'] = CommentForm
    args['user_name'] = auth.get_user(request).username
    return render(request, 'post_detail.html', args)
    '''

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