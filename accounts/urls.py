from django.urls import path

from accounts import views

urlpatterns = [
    path('log-in/', views.LogIn.as_view(), name='log-in'),
    path('sign-up/', views.SignUp.as_view(), name='sign-up'),
]
