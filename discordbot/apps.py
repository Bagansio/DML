from django.apps import AppConfig
#from .models import *
#from .discordbot import *

class DiscordbotConfig(AppConfig):
    name = 'discordbot'
    verbose_name = "My application"
    
    def ready(self):
        from .models import DiscordBot
        print("YOOYO")
        dml = DiscordBot.objects.filter(name='DML').update(init=False)

        
        

        
        