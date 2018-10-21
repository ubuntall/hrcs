from django.contrib import admin

# Register your models here.
from .models import Msg
admin.site.register(Msg)
