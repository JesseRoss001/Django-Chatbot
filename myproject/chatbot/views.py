# chatbot/views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openai
import os

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        if not user_message:
            return JsonResponse({'error': 'No message provided'}, status=400)

        try:
            openai.api_key = os.getenv('OPENAI_API_KEY')
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}]
            )
            bot_response = response.choices[0].message['content']
            return JsonResponse({'message': bot_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # GET request returns a simple form for inputting messages
    return render(request, 'chatbot/chat.html', {
        'title': 'Chat with AI'
    })
