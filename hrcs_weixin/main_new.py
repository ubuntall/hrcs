import os
import sys
import time

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
from bwebsocket import send_last_msg


def msg2db(msg_to_db):
    msg = Msg()
    msg.createTime = msg_to_db.CreateTime
    msg.actualNickName = msg_to_db.actualNickName
    msg.nickName = msg_to_db.User.NickName
    msg.text = msg_to_db.text
    msg.save()
    print("新增了一条数据")
    send_last_msg()


msg_set = set()
msgss = Msg.objects.all()
for msgs in msgss:
    msg_set.add(msgs.text)
print("len(msg_set) = " + str(len(msg_set)))

# n = 0
# for msgs in msgss:
#     for msgz in msgss:
#         try:
#             distance = Levenshtein.distance(msgs.text.strip(), msgz.text.strip())
#             if distance < 65 and distance >= 0:
#                 if n == 0:
#                     n = n + 1
#                 else:
#                     msgz.delete()
#                     print("删除了一条重复数据")
#         except:
#             pass
#     n = 0

keyWords = ["平", "万", "售", "价", "权", "满", "房", "奖", "店", "1"]


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    global msgss
    msg.text = msg.text.strip()
    if msg.text not in msg_set and len(msg.text) < 300:
        msg_set.add(msg.text)
        n = 0
        for k in keyWords:
            if k in msg.text:
                n = n + 1

        if n >= len(keyWords) / 2:
            print("-----------------")
            try:
                Msg.objects.get(text=msg.text)
                print("查询到了一条数据")
                print("len(msg.text) = " + str(len(msg.text)))

            except Msg.DoesNotExist:
                # print(msg)
                # print(msg.CreateTime)
                # print(msg.actualNickName)
                # print(msg.User.NickName)
                # print(msg.text)

                # msgss = Msg.objects.filter(actualNickName=msg.actualNickName)
                # print(msgss)
                n = 0
                distance_min = 299
                for msgs in msgss:
                    distance = Levenshtein.distance(msgs.text.strip(), msg.text)
                    if distance < distance_min:
                        distance_min = distance
                    if distance < 60 and distance >= 0:
                        if n == 0:
                            msgs.text = msg.text
                            msgs.save()
                            n = n + 1
                            print("修改了一条数据")
                        else:
                            msgs.delete()
                            print("删除了一条数据")
                if distance_min < 299:
                    print("distance_min = " + str(distance_min))

                if n == 0:
                    msg2db(msg)
                msgss = Msg.objects.all()


while True:
    try:
        itchat.auto_login(True)
        itchat.run(True)
    except:
        time.sleep(30)
