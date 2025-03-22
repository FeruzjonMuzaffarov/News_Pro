from django.contrib import admin
from .models import Comment



class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


admin.site.register(Comment, CommentAdmin)
