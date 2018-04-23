from django.conf.urls import url

from apps.automata.views import *

urlpatterns = [
    url(r'^$', index, name="index"),	
    url(r'^automata-impar$', automataImpar, name="impar"),	
    url(r'^automata-par$', automataPar, name="par"),	
]