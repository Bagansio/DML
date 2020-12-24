from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django_globals import globals
from django.shortcuts import redirect
from .models import DiscordBot

import os
import json
import requests
import asyncio
import discord
# Create your views here.


def initbot(request: HttpRequest):
    dml = DiscordBot.objects.get(name='DML')
    if(not dml.init):
        DiscordBot.objects.filter(name='DML').update(init=True)
        asyncio.set_event_loop(asyncio.new_event_loop())
        client = discord.Client()

        @client.event
        async def on_ready():
            print('We have logged in as {0.user}'.format(client))

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return

            if message.content.startswith('!hello'):
                await message.channel.send('Hello!')
        f = open('secrets.json')
        data = json.load(f)
        f.close()
        client.run(data["DiscordBot"]["TOKEN"])

        
        print(YOO)
        return redirect("DML/user")
    else:
        print("NO")
        return redirect("DML/user")