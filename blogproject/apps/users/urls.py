from django.urls import path
from .views import register, change_user_role, login_user,home
urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login_user,name='login-user'),
    path('change-role/<int:user_id>/', change_user_role, name='change_user_role'),
    path('',home,name='home')
]
