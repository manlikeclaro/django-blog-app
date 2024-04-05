from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    profile_pic = models.ImageField(upload_to='blog/users/images/', default='')
    bio = models.TextField()
    full_name = models.CharField(max_length=100, default="")

    def save(self, *args, **kwargs):
        self.full_name = f'{self.user.first_name} {self.user.last_name}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.full_name}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Categories"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/posts/images/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="category", null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="posts")
    date = models.DateField(auto_now=True, editable=False)
    slug = models.SlugField(default="", null=False, unique=True)
    excerpt = models.TextField(default="", editable=False)

    # comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.excerpt = self.content[:100]
        super().save()

    def __str__(self):
        return f"{self.title} - {self.author.full_name}"


class BlogComment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(default="")
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="post")
    excerpt = models.TextField(default="")
    date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.excerpt = self.content[:20]
        super().save()

    def __str__(self):
        return f'{self.author.full_name} - {self.excerpt}'
