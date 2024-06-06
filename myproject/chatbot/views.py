# chatbot/views.py
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai

logger = logging.getLogger(__name__)

@csrf_exempt
def chat(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is accepted'}, status=405)

    user_message = request.POST.get('message', '')
    if not user_message:
        return JsonResponse({'error': 'No message provided'}, status=400)

    try:
        openai.api_key = 'your-api-key'  # Make sure this is securely managed
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        return JsonResponse({'message': response.choices[0].message['content']})
    except Exception as e:
        logger.error(f'Error while processing OpenAI API: {str(e)}', exc_info=True)
        return JsonResponse({'error': str(e)}, status=500)
