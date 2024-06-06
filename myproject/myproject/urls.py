from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chatbot.urls')),
    path('', lambda request: redirect('chat/', permanent=False)),  # Redirect root to /chat/
]
