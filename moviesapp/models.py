from django.db import models

from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

# Create your models here.

class Movies(models.Model):

    movie = models.CharField(max_length=64)
    desc = models.TextField()
    director = models.CharField(max_length=64)
    watcher = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    rank = models.IntegerField(default=10)
    
    def __str__(self):
        return self.movie