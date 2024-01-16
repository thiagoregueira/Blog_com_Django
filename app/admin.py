from django.contrib import admin
from app.models import Post


# Register your models here.
@admin.register(Post)
class PostAdimn(admin.ModelAdmin):
    list_display = ("title", "publish", "highlighted", "author")
