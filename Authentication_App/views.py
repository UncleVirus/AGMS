from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms.forms import UserRegistrationForm, UserLoginForm
from django.template import loader
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the HomePage!!!")



# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Registration successful. You can now log in.')
#             return redirect('authentication:login')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'authentication/register.html', {'form': form})
# ###  This register function  handles the user registration. It checks if the requested method is POST, which means that the user has submitted the registration form 
# # If it is a POST request, it validates the form data using the UserRegistrationForm. If the form is valid, it saves the user to the database, displays a success message using Django's messages
# # framework and redirects the user to the login page. If the request method is not POST, it creates a new instance of the UserRegistrationFrom and renders the registration template with the form###


# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 user_login(request, user)
#                 return redirect('home')  
#             else:
#                 messages.error(request, 'Invalid username or password.')
#     else:
#         form = UserLoginForm()
#     return render(request, 'authentication/login.html', {'form': form})

# ### This function handles the user login. Similar to the register function, it checks if the requested method is POST. 
# # If it is, it validates the form data using the UserLoginForm. If the form is valid, it retrieves the username and password from the form's cleaned data.
# # Then it authenticates the user using Django's authenticate function, which checks if the provided credentials are valid. If the user is authenticated successfully, 
# # it logs in using Django's login function and redirects the user to the home page. If the authentication fails, it displays and error message using messages and renders the login template.
# # If the request method is not POST, it creates a new instance of the UserLoginForm and renders the login template with the form ###



# def user_logout(request):
#     logout(request)
#     return redirect('authentication:login')

# ### This function handles user logout. It logs out the currently authenticated user using Django's logout function and redirects the user to the login page. ###