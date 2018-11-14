from django.db import models


# Create your models here.
class Msg(models.Model):
    id = models.AutoField(primary_key=True)
    createTime = models.DateTimeField(auto_now_add=True)
    actualNickName = models.CharField(max_length=100)
    nickName = models.CharField(max_length=100)
    text = models.CharField(max_length=500)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    openId = models.CharField(max_length=100)
    actualNickName = models.CharField(max_length=100)
    chineseName = models.CharField(max_length=100, default="")
    employmentNumber = models.CharField(max_length=100, default="")
    cellPhoneNumber = models.CharField(max_length=100, null=True, default="")
    # companyName = models.CharField(max_length=100, default="")
    # addOnMsg = models.CharField(max_length=100, default="")
    joinTime = models.DateTimeField(auto_now_add=True)


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=500)
    addTime = models.DateTimeField(auto_now_add=True)
    msgId = models.ForeignKey(Msg, on_delete=models.PROTECT, null=True, related_name='msg_id')
    userId = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='user_id')


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=500)
    addTime = models.DateTimeField(auto_now_add=True)
    msgId = models.ForeignKey(Msg, on_delete=models.PROTECT, null=True, related_name='msg_id_in_comment')
    userId = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='user_id_in_comment')


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    imgUrl = models.CharField(max_length=500)
    addTime = models.DateTimeField(auto_now_add=True)
    msgId = models.ForeignKey(Msg, on_delete=models.PROTECT, null=True, related_name='msg_id_in_image')
    userId = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='user_id_in_image')
