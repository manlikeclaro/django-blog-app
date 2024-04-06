from django.urls import path

from blog import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts', views.BlogPosts.as_view(), name='all-posts'),
    path('posts/<slug:slug>', views.SinglePost.as_view(), name='single-post'),
    path('category/<slug:slug>', views.CategoryView.as_view(), name='category'),
    path('about', views.About.as_view(), name='about')
]
