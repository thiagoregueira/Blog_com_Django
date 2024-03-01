from django.contrib import admin
from app.models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdimn(admin.ModelAdmin):
    list_display = ("title", "status", "publish", "highlighted", "author", "slug")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "active", "post")
