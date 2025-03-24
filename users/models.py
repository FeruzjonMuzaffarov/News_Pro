from django.contrib.auth.models import User
from django.db import models
from news.models import News


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    edited_ad = models.DateTimeField(null=True, blank=True)

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return f'{self.user} - {self.content[:30]}...'

