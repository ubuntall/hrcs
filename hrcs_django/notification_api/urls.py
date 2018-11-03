from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_five/', views.get_five, name='get_five'),
    path('get_so/', views.get_so, name='get_so'),
    path('get_item_by_id/', views.get_item_by_id, name='get_item_by_id'),
]
