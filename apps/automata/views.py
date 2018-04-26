# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from apps.automata.models import Automata, AutomataPalindromoImpar

def index(request):
	return render(request, 'automata/index.html')


def automataImpar(request):
	aimpar = Automata.objects.filter(id=1)
	# aimpar = Automata.objects.all()
	context = {"automata": aimpar}
	return render(request, 'automata/automata-impar.html', context)


automata_pi = AutomataPalindromoImpar()


def automataImparEvaluar(request, expression):
	aimpar = Automata.objects.filter(id=1)

	result = automata_pi.validar(expression)

	context = {"automata":aimpar, "expression":expression, "result":result}
	return render(request, 'automata/automata-impar.html', context)

def automataPar(request):
	return render(request, 'automata/automata-par.html')
