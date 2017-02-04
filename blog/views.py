from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comments
from .forms import CommentForm
from django.template.context_processors import csrf
# Create your views here.

def blog(request):
    return render(request, 'blog.html', {'posts': Post.objects.all()})

def post_detail(request, pk):
    args = {}
    args.update(csrf(request))
    args['post'] = get_object_or_404(Post, pk=pk)
    args['comments'] = Comments.objects.filter(comments_post_id = pk)
    args['form'] = CommentForm
    return render(request, 'post_detail.html', args)

def addcomment(request, pk):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_post = Post.objects.get(id=pk)
            form.save()
    return redirect('/blog/post/{}/'.format(pk))