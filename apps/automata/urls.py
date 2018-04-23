from django.conf.urls import url

from apps.automata.views import index

urlpatterns = [
    url(r'^$', index),	
]