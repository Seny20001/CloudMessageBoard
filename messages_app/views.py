from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message

def submit_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_messages')  
    else:
        form = MessageForm()
    return render(request, 'submit_message.html', {'form': form})



def view_messages(request):
    messages = Message.objects.all()  
    return render(request, 'view_messages.html', {'messages': messages})

