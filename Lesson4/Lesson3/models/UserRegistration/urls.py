from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
   
    path('register/', views.register_root, name='users'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
   
    
]