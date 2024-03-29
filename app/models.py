from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import QuerySet
from taggit.managers import TaggableManager


# Create your models here.


class PostManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=175, unique_for_date="publish", blank=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )
    image = models.ImageField(upload_to="imagens/", null=True, blank=True)
    highlighted = models.BooleanField(default=False)
    objects = models.Manager()
    published = PostManager()
    tags = TaggableManager()

    @classmethod
    def get_latest_post(cls, num_post=3):
        return cls.objects.filter(status=cls.Status.PUBLISHED).order_by("-publish")[
            :num_post
        ]

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[self.publish.day, self.publish.month, self.publish.year, self.slug],
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f" {self.title} por {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return f"Comentário de {self.name} em {self.post}"
