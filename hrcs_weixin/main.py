import os
import sys
import django

dir = os.path.dirname(os.path.abspath(__file__))
dir = os.path.join('D:\Workspace\hrcs', 'hrcs_django')
print(dir)
sys.path.insert(0, dir)
settings_path = 'hrcs_django.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_path)
django.setup()

import itchat
from itchat.content import *

from msg2db.models import Msg


def msg2db(CreateTime, actualNickName, NickName, text):
    msg = Msg()
    msg.createTime = CreateTime
    msg.actualNickName = actualNickName
    msg.nickName = NickName
    msg.text = text
    msg.save()
    pass


msg_set = set()


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    keyWords = ["平", "万", "售", "一口价", "产权", "满", "房", "奖", "店", "1"]
    n = 0
    for k in keyWords:
        if k in msg.text:
            n = n + 1

    if n > len(keyWords) / 2:
        if msg.text not in msg_set:
            try:
                msg_set.add(msg.text)
                Msg.objects.get(text=msg.text)
            except Msg.DoesNotExist:
                # print(msg)
                print(msg.CreateTime)
                print(msg.actualNickName)
                print(msg.User.NickName)
                print(msg.text)
                msg2db(msg.CreateTime, msg.actualNickName, msg.User.NickName, msg.text)


itchat.auto_login(True)
itchat.run(True)
