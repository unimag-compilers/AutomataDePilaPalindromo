# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from apps.automata.models import Automata, Expression

admin.site.register(Automata)
admin.site.register(Expression)
