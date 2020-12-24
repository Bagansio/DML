from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context,Template
from discordlogin.models import DiscordUser
from django.contrib.auth.decorators import login_required
from django.template import loader

@login_required(login_url ="/DML/login")
def usermain(request):
    #discord_tag = request.user.discord_tag  #it returns something like Bagansio#8566
    #username = discord_tag[:discord_tag.find('#')]  #it makes that username = Bagansio
    avatar = request.user.avatar_image()
    username = request.user.username()
    tmp = loader.get_template('usermain.html') #load the html
    print(request.user.avatar_image())
    document = tmp.render({"username":username , "avatar_url": avatar}) #render the html with the context
    return HttpResponse(document)