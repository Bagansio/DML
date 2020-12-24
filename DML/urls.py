"""DML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from discordlogin  import views
from discordbot import botviews
from main.views import usermain
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('DML/user', usermain, name='user_main'),
    path('DML', views.home, name = 'DML'),
    path('DML/login', views.discord_login, name='dml_login'),
    path('botini',botviews.initbot, name='initbot'),
    path('DML/login/redirect',views.discord_login_redirect, name='discord_login_redirect'),
] 

urlpatterns += staticfiles_urlpatterns()

