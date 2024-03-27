from datetime import date

from django.shortcuts import render, redirect

blog_posts = [
    {
        "slug": "11-work-from-home-part-time-jobs",
        "image": "post-landscape-1.jpg",
        "author": "Cameron Williamson",
        "date": date(2022, 7, 5),
        "title": "11 Work From Home Part-Time Jobs You Can Do Now",
        "category": "Culture",
        "content": "This is a sample content for the post titled '11 Work From Home Part-Time Jobs You Can Do Now'. "
                   "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus est non ex luctus, "
                   "sed blandit nulla tincidunt. Nam pharetra risus a fermentum aliquet."
    },
    {
        "slug": "lets-get-back-to-work-new-york",
        "image": "post-landscape-2.jpg",
        "author": "Jessica Taylor",
        "date": date(2022, 7, 5),
        "title": "Let’s Get Back to Work, New York",
        "category": "Sport",
        "content": "This is a sample content for the post titled 'Let’s Get Back to Work, New York'. "
                   "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus est non ex luctus, "
                   "sed blandit nulla tincidunt. Nam pharetra risus a fermentum aliquet."
    },
    {
        "slug": "how-to-avoid-distraction-and-stay-focused-during-video-calls",
        "image": "post-landscape-5.jpg",
        "author": "Sarah Moore",
        "date": date(2022, 7, 17),
        "title": "How to Avoid Distraction and Stay Focused During Video Calls?",
        "category": "Business",
        "content": "This is a sample content for the post titled 'How to Avoid Distraction and Stay Focused During "
                   "Video Calls?'. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus est non "
                   "ex luctus, sed blandit nulla tincidunt. Nam pharetra risus a fermentum aliquet."
    },
    {
        "slug": "why-craigslist-tampa-is-one-of-the-most-interesting-places-on-the-web",
        "image": "post-landscape-7.jpg",
        "author": "David Wilson",
        "date": date(2022, 3, 15),
        "title": "Why Craigslist Tampa Is One of The Most Interesting Places On the Web?",
        "category": "Travel",
        "content": "This is a sample content for the post titled 'Why Craigslist Tampa Is One of The Most Interesting "
                   "Places On the Web?'. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus "
                   "est non ex luctus, sed blandit nulla tincidunt. Nam pharetra risus a fermentum aliquet."
    },
    {
        "slug": "6-easy-steps-to-create-your-own-cute-merch-for-instagram",
        "image": "post-landscape-3.jpg",
        "author": "Jane Brown",
        "date": date(2022, 7, 5),
        "title": "6 Easy Steps To Create Your Own Cute Merch For Instagram",
        "category": "Design",
        "content": "This is a sample content for the post titled '6 Easy Steps To Create Your Own Cute Merch For "
                   "Instagram'. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus est non ex "
                   "luctus, sed blandit nulla tincidunt. Nam pharetra risus a fermentum aliquet."
    },
    {
        "slug": "10-life-changing-hacks-every-working-mom-should-know",
        "image": "post-landscape-6.jpg",
        "author": "Michael Johnson",
        "date": date(2022, 3, 1),
        "title": "10 Life-Changing Hacks Every Working Mom Should Know",
        "category": "Tech",
        "content": "This is a sample content for the post titled '10 Life-Changing Hacks Every Working Mom Should Know'. "
                   "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus est non ex luctus, "
                   "sed blandit nulla tincidunt. Nam pharetra risus a fermentum aliquet."
    },
    {
        "slug": "5-great-startup-tips-for-female-founders",
        "image": "post-landscape-8.jpg",
        "author": "Emily Davis",
        "date": date(2022, 7, 5),
        "title": "5 Great Startup Tips for Female Founders",
        "category": "Food",
        "content": "This is a sample content for the post titled '5 Great Startup Tips for Female Founders'. "
                   "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus est non ex luctus, "
                   "sed blandit nulla tincidunt. Nam pharetra risus a fermentum aliquet."
    }
]


def get_date(blog_post):
    return blog_post['date']


# Create your views here.
def index(request):
    # sorted_blog_posts = sorted(blog_posts, key=get_date)
    # latest_posts = sorted_blog_posts[-3:]
    latest_posts = blog_posts[-3:]
    older_posts = blog_posts[1:4]
    response_data = {
        'featured': blog_posts[0],
        'latest': latest_posts,
        'oldest': older_posts,

    }

    return render(request, 'blog/index.html', context=response_data)


def posts(request):
    return render(request, 'blog/all-posts.html')


def single_post(request, slug):
    return render(request, 'blog/single-post.html')


def about(request):
    return render(request, 'blog/about.html')
