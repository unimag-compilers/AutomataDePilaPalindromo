# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Automata(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()


class Expression(models.Model):
	OPTIONS = (
        (0, 'Unknown'),
        (1, 'Yes'),
        (2, 'No'),
    )
	expression = models.CharField(max_length=30, unique=True)
	isPalindrome = models.CharField(max_length=1, choices=OPTIONS, default=0)

	automata = models.ForeignKey(Automata, null=False, blank=False, on_delete=models.CASCADE)