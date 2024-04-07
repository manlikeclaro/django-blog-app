from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='blog/members/images/', default='profile_1.png')
    bio = models.TextField()
    full_name = models.CharField(max_length=100, default="")

    def save(self, *args, **kwargs):
        self.full_name = f'{self.user.first_name} {self.user.last_name}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.full_name}'


class Author(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default='', unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Categories"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/posts/images/', default='post-landscape-1.jpg')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="category", null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    date = models.DateField(auto_now=True, editable=False)
    slug = models.SlugField(default="", null=False, unique=True)
    excerpt = models.TextField(default="", editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.excerpt = self.content[:100]
        super().save()

    def __str__(self):
        return f"{self.title} - {self.author}"


class BlogComment(models.Model):
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField(default="")
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="post")
    excerpt = models.TextField(default="")
    date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.excerpt = self.content[:20]
        super().save()

    def __str__(self):
        return f'{self.author} - {self.excerpt}'
