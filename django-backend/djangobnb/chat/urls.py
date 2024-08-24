from django.urls import path
from . import api

urlpatterns = [
    path('',api.conversations_list,name='api_conversation_list'),
    path('<uuid:pk>/',api.conversations_detail,name='api_conversations_detail'),
    path('start/<uuid:user_id>/',api.conversation_start,name='api_conversation_start')
]