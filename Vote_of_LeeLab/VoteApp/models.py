from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

class VoteDate(models.Model):
    start_date = models.DateTimeField(default=timezone.now())
    end_date = models.DateTimeField(default=(timezone.datetime.now()+timezone.timedelta(days=7))-timezone.timedelta(seconds=1))


class VoteResult(models.Model):
    '''
    DB 시작/종료일, 투표결과를 저장하는 DB를 만들어야 함.
    설계를 해야 하는데 누군가의 도움을 받아야 할 것으로 생각됨.
    따라서 이 부분은 개발일정을 잠정 중단.
    '''
    vote_id = models.ForeignKey(VoteDate, on_delete=models.CASCADE)
    # player = models.ManyToOneRel



class Like(models.Model):
    name_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=8, db_column='이름')
    description = models.CharField(max_length=30, db_column='소개')
    isVote = models.BooleanField(default=False, db_column='후보')
    prize = models.BooleanField(db_column='우승이력', default=False)
    likes = models.ManyToManyField(User, null=True, blank=True, related_name='likes')

    @property
    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        super(Like, self).save(*args, **kwargs)