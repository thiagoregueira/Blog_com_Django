from django.shortcuts import render
from app.models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "post_list.html", context)
