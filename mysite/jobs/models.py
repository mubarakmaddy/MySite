from django.db import models
from django.urls import reverse

class Job(models.Model):
    def get_absolute_url(self):
        return reverse('jobs:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + '-' + self.desc

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
