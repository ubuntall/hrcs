from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_five/', views.get_five, name='get_five'),
    path('get_so/', views.get_so, name='get_so'),
    path('get_item_by_id/', views.get_item_by_id, name='get_item_by_id'),
    path('notes_getall/', views.notes_getall, name='notes_getall'),
    path('note_add/', views.note_add, name='note_add'),
    path('note_update/', views.note_update, name='note_update'),
    path('note_delete/', views.note_delete, name='note_delete'),
    path('note_get/', views.note_get, name='note_get'),
    path('user_add/', views.user_add, name='user_add'),
]
