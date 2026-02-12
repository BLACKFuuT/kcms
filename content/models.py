from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Content(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="contents"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="created_contents"
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to="content_images/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["is_active"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return self.title
