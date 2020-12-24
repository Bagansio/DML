from django.db import models
from .managers import DiscordUserOAuth2Manager

# Create your models here.

class DiscordUser(models.Model):
    objects = DiscordUserOAuth2Manager()

    id = models.BigIntegerField(primary_key=True)
    discord_tag = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100,null=True)
    public_flags = models.IntegerField()
    flags = models.IntegerField()
    locale = models.CharField(max_length=100)
    mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(null=True)

    def is_authenticated(self,request):
        return True 

    def avatar_image(self):
        return 'https://cdn.discordapp.com/avatars/{0}/{1}'.format(self.id,self.avatar)

    def username(self):
        tag = self.discord_tag  #it returns something like Bagansio#8566
        return tag[:tag.find('#')]  #it makes that username = Bagansio