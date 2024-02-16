from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for user registration
    path('register-user/', views.register, name='register_user'),

    # URL pattern for user login
    path('login/', views.login_user, name='login'),

    # URL pattern for user logout
    path('logout/', views.logout_user, name='logout'),

    # URL pattern for user profile
    path('profile/', views.profile, name='profile'),
]
