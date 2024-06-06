# chatbot/views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openai
import os

# Enhanced persona introduction and prompt to visit the website
persona_description = """
Hello! I'm Draco, your guide at CleanDesignUK. Looking to enhance your online presence? Let’s explore how we can transform your ideas into digital realities. Visit us at CleanDesignUK.uk for more information!
"""

contact_details = """
Visit us at 4 Ffordd Cerrig Mawr, Caergeiliog LL65 3LU.
Call us at +44 7367 292269 or email at cleandesign.uk@gmail.com.
Open Mon-Fri: 9:00AM - 5:00PM, Sat-Sun: 10:00AM - 4:00PM.
For more details, visit our website: CleanDesignUK.uk
"""

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        if not user_message:
            return JsonResponse({'error': 'No message provided'}, status=400)

        try:
            openai.api_key = os.getenv('OPENAI_API_KEY')
            # Include contact details and website direction in the initial system message
            messages = [
                {"role": "system", "content": persona_description},
                {"role": "user", "content": user_message}
            ]

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=150
            )
            bot_response = response.choices[0].message['content']

            # Dynamically add contact details if user inquires about contact information or visiting the website
            if "contact" in user_message.lower() or "visit" in user_message.lower() or "website" in user_message.lower():
                bot_response += "\n" + contact_details

            return JsonResponse({'message': bot_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # GET request handling
    return render(request, 'chatbot/chat.html', {
        'title': 'Chat with Draco, the CleanDesignUK Dragon'
    })
