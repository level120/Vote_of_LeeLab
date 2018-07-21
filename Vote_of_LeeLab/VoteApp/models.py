from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Like(models.Model):
    name_id = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 8, db_column='이름')
    description = models.CharField(max_length = 30, db_column='소개')
    isVote = models.BooleanField(default=False, db_column='후보')
    prize = models.BooleanField(db_column='우승이력', default=False)
    likes = models.ManyToManyField(User, null=True, blank=True, related_name='likes')
    # likes = models.ManyToManyField(User, related_name='likes')
    # slug = models.SlugField()
    
    @property
    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.name)
        super(Like, self).save(*args, **kwargs)