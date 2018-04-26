from django.conf.urls import url

from apps.automata.views import *


urlpatterns = [
    url(r'^$', index, name="index"),	
    url(r'^automata-impar/$', automataImpar, name="impar"),	
    url(r'^automata-impar/expresision/([a-c]{1,20})/$', automataImparEvaluar, name="imparEvaluar"),	

    url(r'^automata-par$', automataPar, name="par"),	
    url(r'^automata-par/expresision/([a-b]{1,20})/$', automataParEvaluar, name="parEvaluar"),	
]