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


class AutomataPalindromoImpar:
    pila = ['#']
    tabla = [
        ['f:', 'a', 'b', 'c', '~'],
        [['p','#'], ['p','#a'], ['p','#b'], ['q','#'], ['','']],
        [['p','a'], ['p','aa'], ['p','ab'], ['q','a'], ['','']],
        [['p','b'], ['p','ba'], ['p','bb'], ['q','b'], ['','']],
        [['q','#'], ['',''], ['',''], ['',''], ['r','#']],
        [['q','a'], ['q','~'], ['',''], ['',''], ['','']],
        [['q','b'], ['',''], ['q','~'], ['',''], ['','']],
    ]
    estadoActual = 'p'

    dataTable = {}
 
    def add(self, index, state, rule, stack):
        self.dataTable.setdefault(index,
            {
                "letter":"IDletter-"+index,
                "state":"IDstate-"+state,
                "rule":"ID"+rule,
                "stack":stack
            }
        )

    def top(self):
        return self.pila[-1]

    def popPush(self, apilar):
        self.pila.pop(-1)
        for l in apilar:
            if l != '~' :
                self.pila.append(l)      

    def validar(self, expresion):
        nTransiciones = 0
        cont = 0
        self.dataTable = {}
        for w in expresion :
            cont = cont + 1
            if self.estadoActual == 'p':            
                for f in range(1, 4):
                    if self.tabla[f][0][1] == self.top():
                        for c in range(1,4):
                            if self.tabla[0][c] == w:
                                self.popPush(self.tabla[f][c][1])
                                self.estadoActual = self.tabla[f][c][0]
                                nTransiciones = nTransiciones + 1
                                self.add(str(cont), 'p',w+"_"+self.tabla[f][0][1]+'_'+self.tabla[f][c][1],self.tabla[f][c][1])
                            
                            if nTransiciones == cont: break
                        # endfor
                        if nTransiciones == cont: break
                    # endif
                    # if nTransiciones == cont: break
                # endfor
            elif self.estadoActual == 'q':
                for f in range(4, 7):
                    if self.tabla[f][0][1] == self.top() :
                        for c in range(1,5):
                            if self.tabla[0][c] == w:
                                self.add(str(cont), 'q',w+"_"+self.tabla[f][0][1]+'_'+self.tabla[f][c][1],self.tabla[f][c][1])
                                self.estadoActual = self.tabla[f][c][0]
                                self.popPush(self.tabla[f][c][1])
                                nTransiciones = nTransiciones + 1
                            if nTransiciones == cont: break
                        # endfor
                        if nTransiciones == cont: break
                        
                    # endif
                # endfor
        #endfor
        if self.estadoActual == 'q' and self.top() == '#' and nTransiciones == len(expresion) :
            self.popPush('#')
            self.estadoActual = 'r'
            

        if self.estadoActual == 'r' : 
            self.returnToInitialState()
            return {'isPalindrome':True, 'dataTable':self.dataTable}
        else:
            self.returnToInitialState()
            return {'isPalindrome':False, 'dataTable':self.dataTable}
    # fin funcion validar

    def returnToInitialState(self):
        self.estadoActual = 'p'
        self.pila = ['#']   