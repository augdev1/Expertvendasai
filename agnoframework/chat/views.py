import uuid
import json
from agent_logic import get_agent_response
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from chat.models import Conversation

def new_chat(request):
    conversation = Conversation.objects.create()
    conversation.history.append({'sender': 'bot', 'text': 'Olá, sou o Bryan, sua IA expert em vendas, no que posso ajudar hoje?'})
    conversation.save()
    return redirect('index', conversation_id=conversation.id)

def index(request, conversation_id=None):
    if not conversation_id:
        return redirect('new_chat')

    conversation = get_object_or_404(Conversation, id=conversation_id)
    
    conversations = Conversation.objects.exclude(title__isnull=True).exclude(title__exact='').order_by('-created_at')
    
    return render(request, "chat/index.html", {
        'conversation': conversation,
        'conversations': conversations
    })

def get_response(request, conversation_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('userMessage')

        conversation = get_object_or_404(Conversation, id=conversation_id)

        agent_response = get_agent_response(user_message, conversation_id)

        # Save conversation history
        conversation.history.append({'sender': 'user', 'text': user_message})
        conversation.history.append({'sender': 'bot', 'text': agent_response})
        if not conversation.title and len(conversation.history) > 1:
            conversation.title = conversation.history[1]['text'][:50] + '...'
        conversation.save()

        return JsonResponse({"agentResponse": agent_response})
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def delete_chat(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    conversation.delete()
    return redirect('new_chat')