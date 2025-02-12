from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page to enter interest
    path('chat/<str:interest>/', views.chat_room, name='chat'),  # Chat room page
]
