from django.urls import path
from .views import index, detail, contact, about, category_detail, like_comment, edit_comment

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('contact/', contact, name='contact'),
    path('category/<int:pk>/', category_detail, name='ctg'),
    path('comment/<int:comment_id>/like/', like_comment, name='like_comment'),
    path('edit_comment/<int:comment_id>/', edit_comment, name='edit_comment'),
]