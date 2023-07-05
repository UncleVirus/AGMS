from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms.forms import UserRegistrationForm, UserLoginForm
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'Authentication_App/home.html')






def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Check if the user is registered in the Authentication App
                if user.is_registered:
                    # Redirect to the Artwork Management App
                    return redirect('Artwork_App:artwork_list')
                else:
                    # Redirect to the registration page
                    return redirect('Authentication_App:register')
            else:
                messages.error(request, 'Invalid Username or Password')
    else:
        form = AuthenticationForm()
    return render(request, 'Authentication_App/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Authentication_App:login')
    else:
        form = UserCreationForm()
    return render(request, 'Authentication_App/register.html', {'form': form})





def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('Authentication_App:login')
    return render(request, 'Authentication_App/logout.html')



# ### This function handles user logout. 
# It logs out the currently authenticated user using Django's logout function and redirects the user to the login page. ###

