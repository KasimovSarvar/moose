from django.db import models
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    description = models.TextField()

    author_name = models.CharField(max_length=50, blank=True, null=True)
    author_position = models.CharField(max_length=100, blank=True, null=True)
    author_image = models.ImageField("post_authors/", blank=True, null=True)

    is_published = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def count_comments(self):
        return self.comments.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=128)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"



class Contact(models.Model):
    full_name = models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    is_solved = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"