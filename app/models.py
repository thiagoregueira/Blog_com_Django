from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
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
    slug = models.SlugField(max_length=175)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )
    image = models.ImageField(upload_to="imagens/", null=True, blank=True)
    highlighted = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.title} por {self.author}"
