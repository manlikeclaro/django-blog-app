from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='blog/members/images/', default='blog/members/images/default-user.png')
    bio = models.TextField()
    full_name = models.CharField(max_length=100, default="")

    def save(self, *args, **kwargs):
        self.full_name = f'{self.user.first_name} {self.user.last_name}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.full_name}'


class Author(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, default='')
    posts_count = models.IntegerField(default=0)

    # def save(self, *args, **kwargs):
    #     # self.posts_count = self.posts.count()
    #     super().save()

    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default='', unique=True)
    posts_count = models.IntegerField(default=0)

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
    image = models.ImageField(upload_to='blog/posts/images/', default='blog/posts/images/default-blog.png')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="category", null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    date = models.DateField(auto_now=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField(default="", null=False, unique=True)
    excerpt = models.TextField(default="", editable=False)

    def save(self, *args, **kwargs):
        is_new_post = not self.pk  # Check if the BlogPost is being created or updated
        self.slug = slugify(self.title)
        # self.excerpt = self.content[:100]
        split_content = self.content.split()
        excerpt_content = split_content[:15]  # Slicing first 15 words for excerpt
        self.excerpt = f'{' '.join(excerpt_content)}...'

        # self.author.save()
        super().save()

        if is_new_post:  # If this is a new BlogPost being created
            category = self.category
            author = self.author
            category.posts_count = BlogPost.objects.filter(category=category).count()
            author.posts_count = BlogPost.objects.filter(author=author).count()  # Update the posts_count field
            category.save()
            author.save()  # Save the updated Author instance

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
