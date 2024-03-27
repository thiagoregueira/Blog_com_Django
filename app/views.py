from django.shortcuts import render, get_object_or_404
from app.models import Post
from app.forms import CommentForm
from django.views.decorators.http import require_POST

# Create your views here.


# listar todos os posts
def post_list(request):
    posts = Post.published.all()
    latest_posts = Post.get_latest_post(3)
    context = {
        "posts": posts,
        "latest_posts": latest_posts,
    }
    return render(request, "post_list.html", context)


# listar um post específico
def post_detail(request, day, month, year, slug):
    post = get_object_or_404(
        Post, publish__day=day, publish__month=month, publish__year=year, slug=slug
    )
    latest_posts = Post.get_latest_post(3)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    context = {
        "post": post,
        "latest_posts": latest_posts,
        "comments": comments,
        "form": form,
    }
    return render(request, "post_detail.html", context)


@require_POST
def post_comment(request, id):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, id=id)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    else:
        comment = None
    context = {
        "post": post,
        "comment": comment,
        "form": form,
    }
    return render(request, "comment_success.html", context)
