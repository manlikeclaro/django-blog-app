from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from blog.forms import BlogCommentModelForm
from blog.models import BlogPost, BlogComment, Category


# Create your views here.
class IndexView(View):
    all_blog_posts = BlogPost.objects.all()
    categories = Category.objects.all()

    def get(self, request):
        hero_blog_posts = self.all_blog_posts[:4]
        featured_blog_post = self.all_blog_posts.first()
        latest_blog_posts = self.all_blog_posts.order_by('-date')[:3]  # Get the latest 3 blog posts
        oldest_blog_posts = self.all_blog_posts.order_by('date')[:3]  # Get the oldest 3 blog posts

        context = {'hero': hero_blog_posts, 'featured': featured_blog_post, 'latest': latest_blog_posts,
                   'oldest': oldest_blog_posts, 'categories': self.categories}
        return render(request, 'blog/index.html', context)


class BlogPosts(View):
    all_blog_posts = BlogPost.objects.all()
    categories = Category.objects.all()

    def get(self, request):
        latest_blog_posts = self.all_blog_posts.order_by('-date')

        context = {'posts': latest_blog_posts, 'categories': self.categories}
        return render(request, 'blog/all-posts.html', context)


class SinglePost(View):
    categories = Category.objects.all()

    def get(self, request, slug):
        form = BlogCommentModelForm()
        identified_blog_post = get_object_or_404(BlogPost, slug=slug)
        comments = BlogComment.objects.filter(blog_post=identified_blog_post).order_by('-date')

        context = {'post': identified_blog_post, 'comments': comments, 'form': form, 'categories': self.categories}
        return render(request, 'blog/single-post.html', context)

    def post(self, request, slug):
        form = BlogCommentModelForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.member
            comment.blog_post = get_object_or_404(BlogPost, slug=slug)
            comment.save()
            return redirect('single-post', slug)

        # context = {'post': identified_blog_post, 'comments': comments, 'form': form, 'categories': categories}
        # return render(request, 'blog/single-post.html', context)


class About(View):
    categories = Category.objects.all()

    def get(self, request, ):
        context = {'categories': self.categories, }
        return render(request, 'blog/about.html')


class CategoryView(View):
    categories = Category.objects.all()

    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        blogposts = BlogPost.objects.filter(category=category)
        context = {'category': category, 'categories': self.categories, 'posts': blogposts}
        return render(request, 'blog/category.html', context)
