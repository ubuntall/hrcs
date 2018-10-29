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
from django.shortcuts import render
from dwebsocket.decorators import accept_websocket, require_websocket
from django.http import HttpResponse
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
            for message in request.websocket:
                if not message:
                    break
                for client in clients:
                    client.send(message)
        finally:
            clients.remove(request.websocket)
            lock.release()  # 释放锁


@accept_websocket
def echo(request):
    if not request.is_websocket():  # 判断是不是websocket连接
        try:  # 如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request, 'index.html')
    else:
        for message in request.websocket:
            request.websocket.send(message)  # 发送消息到客户端


@require_websocket
def send_last_msg(request):
    if request.is_websocket:  # 如果是webvsocket
        message = Msg.objects.last()
        request.websocket.send(message)
