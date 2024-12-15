from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_message, name='submit_message'),
    path('messages/', views.view_messages, name='view_messages'),
]
