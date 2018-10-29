import os
import sys
import threading

import django

dir = os.path.dirname(os.path.abspath(__file__))
dir = os.path.join('D:\Workspace\hrcs', 'hrcs_django')
print(dir)
sys.path.insert(0, dir)
settings_path = 'hrcs_django.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_path)
django.setup()
# Create your views here.
from dwebsocket.decorators import accept_websocket, require_websocket
from msg2db.models import Msg

# Create your views here.

clients = []


@require_websocket
def notification(request):
    if request.is_websocket:  # 如果是webvsocket
        lock = threading.RLock()  # rlock线程锁
        try:
            lock.acquire()  # 抢占资源
            clients.append(request.websocket)  # 把websocket加入到clients
            print(clients)
            message = Msg.objects.last()
            if not message:
                print("还没有入库的消息")
            for client in clients:
                client.send(message)
        finally:
            clients.remove(request.websocket)
            lock.release()  # 释放锁


@require_websocket
def send_last_msg(request):
    if request.is_websocket:  # 如果是webvsocket
        message = Msg.objects.last()
        request.websocket.send(message)


@accept_websocket
def index(request):
    if request.is_websocket:  # 如果是webvsocket
        # message = bytes(Msg.objects.last())

        message = Msg.objects.last().text
        request.websocket.send(message)
@require_websocket
def echo_once(request):
    message = request.websocket.wait()
    request.websocket.send(message)
