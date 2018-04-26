# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from apps.automata.models import Automata, AutomataPalindromoImpar, AutomataPalindromePar

def index(request):
	return render(request, 'automata/index.html')


def automataImpar(request):
	automata_impar = Automata.objects.filter(id=1)
	# automata_impar = Automata.objects.all()
	context = {"automata": automata_impar}
	return render(request, 'automata/automata-impar.html', context)


automata_pi = AutomataPalindromoImpar()

def automataImparEvaluar(request, expression):
	automata_impar = Automata.objects.filter(id=1)

	result = automata_pi.validar(expression)

	context = {"automata":automata_impar, "expression":expression, "result":result}
	return render(request, 'automata/automata-impar.html', context)

def automataPar(request):
	automata_par = Automata.objects.filter(id=2)
	# automata_par = Automata.objects.all()
	context = {"automata": automata_par}
	return render(request, 'automata/automata-par.html', context)


automata_pp = AutomataPalindromePar()

def automataParEvaluar(request, expression):
	automata_par = Automata.objects.filter(id=2)

	result = automata_pp.validar(expression)

	context = {"automata":automata_par, "expression":expression, "result":result}
	return render(request, 'automata/automata-par.html', context)
