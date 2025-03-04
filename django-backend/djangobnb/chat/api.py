from rest_framework.decorators import api_view,permission_classes,renderer_classes,authentication_classes
from django.http import JsonResponse
from .serializers import ConversationListSerializer,ConversationDetailSerializer,ConversationMessageSerializer
from .models import Conversation,ConversationMessage
from useraccount.models import User
@api_view(['GET'])
def conversations_list(request):
    serializer = ConversationListSerializer(request.user.conversations.all(),many = True)
    return JsonResponse(serializer.data,safe=False)


@api_view(['GET'])
def conversations_detail(request,pk):

    conversation = request.user.conversations.get(pk=pk)
    conversation_serializer = ConversationDetailSerializer(conversation,many = False)
    messages_serializer = ConversationMessageSerializer(conversation.messages.all(),many = True)
    return JsonResponse({
        'conversation':conversation_serializer.data,
        'messages':messages_serializer.data

    },safe=False)


@api_view(['GET'])
def conversation_start(request,user_id):
    conversations = Conversation.objects.filter(users__in = [user_id]).filter(users__in=[request.user.id])

    if conversations.count() > 0:
        conversation = conversations.first()
        return JsonResponse(
            {
                'success':'already in a conversation','conversation_id':conversation.id
            }
        )
    else:
        user = User.objects.get(pk = user_id)
        conversation = Conversation.objects.create()
        conversation.users.add(user)
        conversation.users.add(request.user)
        
        return JsonResponse(
            {
                'success':'conversation created','conversation_id':conversation.id
            }
        )

