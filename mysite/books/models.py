from django.db import models

# Create your models here.
#DB

class Book(models.Model):

    def __str__(self):
        return self.name + '-' + self.author

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class FavouriteBooks(models.Model):
    bookid = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
