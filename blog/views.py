from datetime import date

from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import BlogCommentModelForm
from blog.models import BlogPost, BlogComment

blog_posts = [
    {
        "slug": "11-work-from-home-part-time-jobs",
        "image": "post-landscape-1.jpg",
        "author": "Cameron Williamson",
        "date": date(2022, 7, 5),
        "title": "11 Work From Home Part-Time Jobs You Can Do Now",
        "category": "Career",
        "content": "This post explores 11 legitimate part-time jobs suitable for remote work, offering flexibility and opportunities for those seeking work-from-home options.",
        "excerpt": "Discover 11 part-time remote job opportunities providing flexibility and work-life balance."
    },
    {
        "slug": "lets-get-back-to-work-new-york",
        "image": "post-landscape-2.jpg",
        "author": "Jessica Taylor",
        "date": date(2022, 7, 5),
        "title": "Let’s Get Back to Work, New York",
        "category": "Business",
        "content": "This article discusses the resurgence of business activities in New York, analyzing the city's economic recovery efforts and the return to office culture post-pandemic.",
        "excerpt": "Explore New York's economic revival and the resurgence of office culture post-pandemic."
    },
    {
        "slug": "how-to-avoid-distraction-and-stay-focused-during-video-calls",
        "image": "post-landscape-5.jpg",
        "author": "Sarah Moore",
        "date": date(2022, 7, 17),
        "title": "How to Avoid Distraction and Stay Focused During Video Calls?",
        "category": "Productivity",
        "content": "This post provides practical tips and strategies to minimize distractions and enhance focus during video calls, crucial for maintaining productivity in remote work settings.",
        "excerpt": "Learn effective strategies to stay focused and productive during video calls."
    },
    {
        "slug": "why-craigslist-tampa-is-one-of-the-most-interesting-places-on-the-web",
        "image": "post-landscape-7.jpg",
        "author": "David Wilson",
        "date": date(2022, 3, 15),
        "title": "Why Craigslist Tampa Is One of The Most Interesting Places On the Web?",
        "category": "Technology",
        "content": "Delve into the fascinating aspects of Craigslist Tampa, exploring its unique features and the diverse range of interactions that make it a compelling online destination.",
        "excerpt": "Explore the intriguing features that make Craigslist Tampa an interesting online hub."
    },
    {
        "slug": "6-easy-steps-to-create-your-own-cute-merch-for-instagram",
        "image": "post-landscape-3.jpg",
        "author": "Jane Brown",
        "date": date(2022, 7, 5),
        "title": "6 Easy Steps To Create Your Own Cute Merch For Instagram",
        "category": "Design",
        "content": "This guide offers a step-by-step approach to designing and creating appealing merchandise for Instagram, catering to individuals looking to monetize their creative endeavors.",
        "excerpt": "Learn how to design and create attractive merchandise for Instagram in 6 simple steps."
    },
    {
        "slug": "10-life-changing-hacks-every-working-mom-should-know",
        "image": "post-landscape-6.jpg",
        "author": "Michael Johnson",
        "date": date(2022, 3, 1),
        "title": "10 Life-Changing Hacks Every Working Mom Should Know",
        "category": "Parenting",
        "content": "Discover practical and innovative life hacks tailored to assist working mothers in managing their professional responsibilities while balancing family commitments effectively.",
        "excerpt": "Explore 10 ingenious life hacks designed to help working moms achieve better work-life balance."
    },
    {
        "slug": "5-great-startup-tips-for-female-founders",
        "image": "post-landscape-8.jpg",
        "author": "Emily Davis",
        "date": date(2022, 7, 5),
        "title": "5 Great Startup Tips for Female Founders",
        "category": "Entrepreneurship",
        "content": "This article offers valuable insights and tips specifically curated for female entrepreneurs embarking on startup ventures, addressing common challenges and providing actionable advice for success.",
        "excerpt": "Get expert advice and insights tailored for female entrepreneurs starting their own businesses."
    }
    # Add more records as needed
]


# Create your views here.
def index(request):
    all_blog_posts = BlogPost.objects.all()
    featured_blog_post = BlogPost.objects.first()

    # Get the latest 3 blog posts
    latest_blog_posts = all_blog_posts.order_by('-date')[:3]

    # Get the oldest 3 blog posts
    oldest_blog_posts = all_blog_posts.order_by('date')[:3]

    response_data = {
        'featured': featured_blog_post,
        'latest': latest_blog_posts,
        'oldest': oldest_blog_posts,

    }

    return render(request, 'blog/index.html', context=response_data)


def posts(request):
    all_blog_posts = BlogPost.objects.all()
    # Get the latest blog posts
    latest_blog_posts = all_blog_posts.order_by('-date')
    response_data = {
        # 'posts': latest_posts,
        'posts': latest_blog_posts,

    }
    return render(request, 'blog/all-posts.html', context=response_data)


def single_post(request, slug):
    identified_blog_post = get_object_or_404(BlogPost, slug=slug)
    comments = BlogComment.objects.filter(blog_post=identified_blog_post)

    form = BlogCommentModelForm(request.POST)
    if form.is_valid():
        # form.save()
        comment = form.save(commit=False)
        comment.blog_post = identified_blog_post
        comment.save()
        return redirect('single-post', slug)

    response_data = {
        # 'post': identified_post,
        'post': identified_blog_post,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog/single-post.html', context=response_data)


def about(request):
    return render(request, 'blog/about.html')
