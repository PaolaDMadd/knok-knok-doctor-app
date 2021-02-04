from users import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile')
]