from django.shortcuts import render

def home(request):
    return render(request, "Chatapp/home.html")  # Render home.html

def chat_room(request, interest):
    return render(request, "Chatapp/chat.html", {"interest": interest})  # Pass interest to chat.html
