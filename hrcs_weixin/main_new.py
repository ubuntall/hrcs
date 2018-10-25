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
import Levenshtein
from itchat.content import *
from msg2db.models import Msg


def msg2db(msg_to_db):
    msg = Msg()
    msg.createTime = msg_to_db.CreateTime
    msg.actualNickName = msg_to_db.actualNickName
    msg.nickName = msg_to_db.User.NickName
    msg.text = msg_to_db.text
    msg.save()
    print("msg2db() Susscess")


msg_set = set()

keyWords = ["平", "万", "售", "一口价", "产权", "满", "房", "奖", "店", "1"]


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    msg.text = msg.text.strip()
    if msg.text not in msg_set:
        msg_set.add(msg.text)
        n = 0
        for k in keyWords:
            if k in msg.text:
                n = n + 1

        if n > len(keyWords) / 2:
            try:
                Msg.objects.get(text=msg.text)

            except Msg.DoesNotExist:
                # print(msg)
                print(msg.CreateTime)
                print(msg.actualNickName)
                print(msg.User.NickName)
                print(msg.text)
                msg2db(msg)

                msgss = Msg.objects.filter(actualNickName=msg.actualNickName)
                # print(msgss)
                for msgs in msgss:
                    distance = Levenshtein.distance(msgs.text, msg.text)
                    print("distance = " + str(distance))
                    if distance < 5 and distance > 0:
                        msgs.delete()


itchat.auto_login(True)
itchat.run(True)
