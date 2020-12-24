from django.db import models
#from .dscbot import DiscordBotManager
# Create your models here.

class DiscordBot(models.Model):
    #objects = DiscordBotManager()
    name = models.CharField(max_length=30)
    init = models.BooleanField(null=False)
