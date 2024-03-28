from django.db import models
from django.utils.text import slugify


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100, default="")

    def save(self, *args, **kwargs):
        self.full_name = f'{self.first_name} {self.last_name}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.full_name}'


class BlogPost(models.Model):
    slug = models.SlugField(default="", null=False)
    # image = models.ImageField(upload_to='blog_images/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="posts")
    date = models.DateField()
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    content = models.TextField()
    excerpt = models.TextField(default="", editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.excerpt = self.content[:100]
        super().save()

    def __str__(self):
        return self.title
