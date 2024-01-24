from django.shortcuts import render, get_object_or_404
from app.models import Post

# Create your views here.


# listar todos os posts
def post_list(request):
    posts = Post.published.all()
    context = {
        "posts": posts,
    }
    return render(request, "post_list.html", context)


# listar um post específico
def post_detail(request, day, month, year, slug):
    post = get_object_or_404(
        Post, publish__day=day, publish__month=month, publish__year=year, slug=slug
    )
    context = {
        "post": post,
    }
    return render(request, "post_detail.html", context)
