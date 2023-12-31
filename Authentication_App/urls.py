from django.urls import path
from . import views

app_name = 'Authentication_App'

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
