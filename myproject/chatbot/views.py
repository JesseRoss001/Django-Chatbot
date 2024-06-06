from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai

@csrf_exempt  # To simplify, better to handle CSRF in production
def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        # Assuming 'openai.ChatCompletion.create' is how you interface with GPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_response = response.choices[0].message['content'] if response.choices else "Sorry, I didn't get that."
        return JsonResponse(bot_response, safe=False)

    return render(request, 'chatbot/chat.html')

