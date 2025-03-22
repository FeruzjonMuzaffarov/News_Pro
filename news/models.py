from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField()
    image = models.ImageField(upload_to='news_images/', default='default/default.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.category.name}"


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sponsor_images/')
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    view = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Contacts"
        ordering = ['view']

    def __str__(self):
        return f"{self.name} - {self.email}"

