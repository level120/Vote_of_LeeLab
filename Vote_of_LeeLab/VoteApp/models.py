from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Like(models.Model):
    name_id = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')
    disLikes = models.ManyToManyField(User, related_name='disLikes')
    
    @property
    def total_likes(self):
        return self.likes.count()
    
    @property
    def total_disLikes(self):
        return self.disLikes.count()