from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
#DB


class Book(models.Model):
    def __str__(self):
        return self.name + '-' + self.author

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    book_image = models.CharField(max_length=1000)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('books:index')


class FavouriteBooks(models.Model):
    bookid = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
