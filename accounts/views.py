from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from accounts.forms import LoginForm, SignUpForm
from blog.models import Member


# Create your views here.
class SignUp(View):
    def get(self, request):
        form = SignUpForm()

        context = {'form': form}
        return render(request, 'accounts/registration.html', context)

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # Create Customer instance associated with the user
            # phone_number = form.cleaned_data['phone_number']
            member = Member.objects.create(user=user, )

            # Authenticate the user after saving the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.username.title()}! You have successfully signed up.')
                return redirect('index')
        else:
            context = {'form': form}
            return render(request, 'accounts/registration.html', context)


class LogIn(View):
    def get(self, request):
        form = LoginForm()

        context = {'form': form}
        return render(request, 'accounts/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username.title()}! You have successfully logged in.')

                next_page = request.POST.get('next', '')  # Get the 'next' parameter from POST data
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect('home')  # Redirect to 'home' if 'next' parameter is not provided
            else:
                messages.error(request, 'Invalid username or password')

        context = {'form': form}
        return render(request, 'accounts/login.html', context)
