from django.db import models


# Create your models here.
class Msg(models.Model):
    id = models.AutoField(primary_key=True)
    createTime = models.DateTimeField(auto_now_add=True)
    actualNickName = models.CharField(max_length=200)
    nickName = models.CharField(max_length=200)
    text = models.CharField(max_length=9999)
