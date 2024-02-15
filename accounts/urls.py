from django.urls import path
from . import views

urlpatterns = [
     path('register-user/',views.register,name = 'register_user'),
     path('login/',views.login_user,name = 'login'),
     path('logut/',views.logout_user, name = 'logut'),
]
