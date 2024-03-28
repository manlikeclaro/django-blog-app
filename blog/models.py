from django.db import models
from django.utils.text import slugify


# Create your models here.
class BlogPost(models.Model):
    slug = models.SlugField(default="", null=False)
    # image = models.ImageField(upload_to='blog_images/')
    author = models.CharField(max_length=100)
    date = models.DateField()
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    content = models.TextField()
    excerpt = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.excerpt = self.content[:100]
        super().save()

    def __str__(self):
        return self.title
