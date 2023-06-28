from django.urls import path
from . import views

app_name = 'Authentication_App'

urlpatterns = [

    path('', views.home, name='home'),


    # path('register/', views.register, name='register'),
    # path('user_login/', views.login, name='user_login'),
    # path('user_logout/', views.logout, name='user_logout'),
]
