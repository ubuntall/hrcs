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
    json_data = serialize('json', Msg.objects.all().order_by('-id')[:5])
    return HttpResponse(json.dumps(json_data), content_type="application/json")


def get_so(request):
    keyword = request.GET.get("keyword")
    json_data = serialize('json', Msg.objects.filter(Q(text__contains=keyword) | Q(actualNickName__contains=keyword)))
    return HttpResponse(json.dumps(json_data), content_type="application/json")
