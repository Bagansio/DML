from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required

import requests

# Create your views here.

#auth_url_discord used to login in the app
auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=784193418817175552&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2FDML%2Flogin%2Fredirect&response_type=code&scope=identify"

def home(request: HttpRequest) -> HttpResponse:
    return JsonResponse({ "msg": "Hello"})

def discord_login(request: HttpRequest):
    return redirect(auth_url_discord)

def discord_login_redirect(request: HttpRequest):
    code = request.GET.get('code')
    user = exchange_code(code)

    discord_user = authenticate(request, user = user)  #authenticate the discord user 
    discord_user = list(discord_user).pop()
    print(discord_user)
    login(request, discord_user)                       #login the discord user
    return redirect("/DML/user")                       #redirecto to DML/user

def exchange_code(code: str): #extracts the user data
    data = {
        "client_id": "784193418817175552",
        "client_secret": "N0x3wA4YNeWpHf1E4GlsdK1eXP2A0sgq",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/DML/login/redirect",
        "scope": "identify"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post("https://discord.com/api/oauth2/token",data=data,headers=headers)
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get("https://discord.com/api/v6/users/@me", headers={
        'Authorization': 'Bearer %s' % access_token
    })
    user = response.json()
    return user