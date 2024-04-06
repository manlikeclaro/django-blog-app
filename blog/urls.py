from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='all-posts'),
    path('posts/<slug:slug>', views.single_post, name='single-post'),
    path('category/<slug:slug>', views.CategoryView.as_view(), name='category'),
    path('about', views.about, name='about')
]
