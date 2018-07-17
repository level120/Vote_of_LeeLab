from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Like(models.Model):
    name_id = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 8, db_column='이름')
    prize = models.BooleanField(db_column='우승이력')
    prize_date = models.DateTimeField(null=True)
    likes = models.ManyToManyField(User, related_name='likes')
    
    @property
    def total_likes(self):
        return self.likes.count()

    def generate(self):
        self.prize_date = timezone.now()
        self.save()

    def __str__(self):
        context = ""
        if self.prize:
            context = '%s - 우승전적 있음(마지막 수상일 : %s)' % (self.name, )
        else:
            context = '%s' % (self.name)
        return context