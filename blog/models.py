from django.db import models
from django.utils.text import slugify


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    full_name = models.CharField(max_length=100, default="")

    def save(self, *args, **kwargs):
        self.full_name = f'{self.first_name} {self.last_name}'
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
    slug = models.SlugField(default="", null=False, unique=True)
    # image = models.ImageField(upload_to='blog_images/')
    image = models.CharField(max_length=100, default="post-landscape-1.jpg", null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="posts")
    date = models.DateField(auto_now=True, editable=False)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="category", null=True)
    content = models.TextField()
    excerpt = models.TextField(default="", editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.excerpt = self.content[:100]
        super().save()

    def __str__(self):
        return self.title
