import os
import sys

import django
from django.db.models import Q

dir = os.path.dirname(os.path.abspath(__file__))
dir = os.path.join('D:\Workspace\hrcs', 'hrcs_django')
print(dir)
sys.path.insert(0, dir)
settings_path = 'hrcs_django.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_path)
django.setup()
# Create your views here.
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
import json
from msg2db.models import Msg
from msg2db.models import Note
from msg2db.models import User


def index(request):
    msg = Msg.objects.last()
    json_data = {"id": msg.id, "actualNickName": msg.actualNickName, "nickName": msg.nickName, "text": msg.text}
    return HttpResponse(json.dumps(json_data), content_type="application/json")


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Msg):
            return str(obj)
        return super().default(obj)


def get_five(request):
    # json_data = serialize('json', Msg.objects.all().order_by('-id')[:5], cls=LazyEncoder)
    json_data = serialize('json', Msg.objects.all().order_by('-id')[:10])
    return HttpResponse(json.dumps(json_data), content_type="application/json")


def get_so(request):
    keyword = request.GET.get("keyword")
    json_data = serialize('json', Msg.objects.filter(Q(text__contains=keyword) | Q(actualNickName__contains=keyword)))
    return HttpResponse(json.dumps(json_data), content_type="application/json")


def get_item_by_id(request):
    id = request.GET.get("id")
    json_data = serialize('json', Msg.objects.filter(id=id))
    return HttpResponse(json.dumps(json_data), content_type="application/json")


def notes_getall(request):
    openId = request.GET.get("openId")
    user = User.objects.get(openId=openId)
    json_data = serialize('json', Note.objects.filter(userId=user.id))
    return HttpResponse(json.dumps(json_data), content_type="application/json")


def note_get(request):
    noteId = request.GET.get("noteId")
    json_data = serialize('json', Note.objects.filter(noteId=noteId))
    return HttpResponse(json.dumps(json_data), content_type="application/json")


def note_add(request):
    openId = request.GET.get("openId")
    msgId = request.GET.get("msgId")
    try:
        note = Note.objects.get(msgId=msgId)
    except Note.DoesNotExist:
        try:
            user = User.objects.get(openId=openId)
        except User.DoesNotExist:
            user = User()
            user.openId = openId
            user.save()
        msg = Msg.objects.get(id=msgId)
        note = Note()
        note.userId = user
        note.msgId = msg
        note.text = msg.text
        note.save()
        json_data = serialize('json', [note, ])
        return HttpResponse(json.dumps(json_data), content_type="application/json")


def note_update(request):
    noteId = request.GET.get("noteId")
    text = request.GET.get("text")
    note = Note()
    note.noteId = noteId
    note.text = text
    note.save()
    if note.id > 0:
        response = "1"
    else:
        response = "0"
    json_data = serialize('json', response)
    return HttpResponse(json.dumps(json_data), content_type="application/json")


def note_delete(request):
    noteId = request.GET.get("noteId")
    openId = request.GET.get("openId")
    user = User.objects.get(openId=openId)
    note = Note.objects.get(id=noteId, userId=user.id)
    note.delete()
    json_data = serialize('json', [note, ])
    return HttpResponse(json.dumps(json_data), content_type="application/json")


def user_add(request):
    openId = request.GET.get("openId")
    try:
        user = User.objects.get(openId=openId)
    except User.DoesNotExist:
        user = User()
        user.openId = openId
        user.save()
    json_data = serialize('json', [user, ])
    return HttpResponse(json.dumps(json_data), content_type="application/json")
