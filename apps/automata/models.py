# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Automata(models.Model):
	name = models.CharField(max_length=60)
	description = models.TextField()


class Expression(models.Model):
	OPTIONS = (
        ('unknown', 'No definido'),
        ('true', 'Si'),
        ('false', 'No'),
    )
	expression = models.CharField(max_length=30, unique=True)
	isPalindrome = models.CharField(max_length=1, choices=OPTIONS, default='unknown')

	automata = models.ForeignKey(Automata, null=False, blank=False, on_delete=models.CASCADE)