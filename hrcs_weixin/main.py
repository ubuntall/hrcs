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
    if '平' in msg.text and '万' in msg.text:
        if msg.text not in msg_set:
            msg_set.add(msg.text)
            # print(msg)
            print(msg.CreateTime)
            print(msg.actualNickName)
            print(msg.User.NickName)
            print(msg.text)
            msg2db(msg.CreateTime, msg.actualNickName, msg.User.NickName, msg.text)


itchat.auto_login(True)
itchat.run(True)
