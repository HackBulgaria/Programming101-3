from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import ChatMessage

def chat_logout(request):
    logout(request)
    return redirect("index")


def index(request):
    if request.user.is_authenticated():
        return redirect("chat")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
           login(request, user) 
           return redirect("chat")
        else:
            return redirect("index")

    else:
        return render(request, "index.html", locals())

@login_required(login_url="index")
def chat(request):
    if request.method == "POST":
        message = request.POST.get("message")
        user = request.user
            
        user.chatmessage_set.add(ChatMessage(message=message))
        user.save()
        return redirect("chat")
    else:
        messages = ChatMessage.objects.all()
        logged_users = User.objects.all()
        return render(request, "chat.html", locals())


def _validate_register(username, email, password):
    if username is None or username.strip() == "":
        return False
    
    if email is None or email.strip() == "":
        return False

    if password is None or password.strip() == "":
        return False

    return True


def register(request):
    if request.user.is_authenticated():
        return redirect("chat")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if not _validate_register(username, email, password):
            return HttpResponseBadRequest("Something is missing")
        
        user = User.objects.create_user(username, email, password)
        return redirect("index")

    else:
        return render(request, "register.html", locals())













