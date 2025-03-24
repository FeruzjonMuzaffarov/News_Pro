from django.urls import path
from .views import register, login_user, logout_user, profile_view, delete_comment

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('delete_comment/<int:pk>/', delete_comment, name='delete_comment'),
]