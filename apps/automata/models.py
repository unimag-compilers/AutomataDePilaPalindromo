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




class AutomataPalindromePar : 
    dic = {
        "p": {
            "a":{
                "b": { 0:["p", "ba"] },
                "a": { 
                    0:["p", "aa"],
                    1:["q", "~"]
                },
                "#": { 0:["p", "#a"] }
            },
            "b":{
                "b": { 
                    0:["p", "bb"],
                    1:["q", "~" ]
                },
            "a": { 0:["p", "ab"] },
            "#": { 0:["p", "#b"] }
            }
        },
        "q": {
            "b":{ 
                "b":{ 0:["q", "~"] }
            },
            "a":{
                "a":{ 0:["q", "~"] }
            },
            "~":{
                "#":{ 0:["r", "#"] }
            }
        }

    }
    
    pila = ['#']
    estado = 'p'
    versions  = []

    dataTable = {}
 
    def add(self, index, state, rule, stack):
        index2 = index
        if index in self.dataTable :
            index = len(self.dataTable)+1
            index = str(index) 
        self.dataTable.setdefault(index,
            {
                "letter":"IDletter-"+index2,
                "state":"IDstate-"+state,
                "rule":"ID"+rule,
                "stack":stack
            }
        )

    def setPila(self, newValue):
        self.pila = newValue

    def top(self):
        return self.pila[-1]

    def popPush(self, apilar):
        self.pila.pop()
        for l in apilar:
            if l != '~' :
                self.pila.append(l)

    def returnToInitialState(self):
        self.estado = 'p'
        self.pila = ['#']
        self.versions = []
            
    def saveVersion(self, i, pila, estado, usada):
        self.versions.append(
            {
                'i' : i,
                'pila' : pila,
                'estado' : estado,
                'usada' : usada
            }
        )
        
    def verDatos(self, i, cont, nTransiciones):
        print("-------------------------------")
        print("estado=",self.estado)
        print("pila=",self.pila)
        print("i=",i)
        print("conta=",cont)
        print("nTransiciones=",nTransiciones)
        print("-------------------------------")
    
    def used(self):
        return self.versions[-1]['usada']
    
    def validar(self, expresion):
        nTransiciones = 0
        cont = 0
        i = 0
        self.restorePoint = []
        fin = False
        self.dataTable = {}
        while i < len(expresion) :            
            cont = cont + 1 
            if self.estado == 'p':
                if expresion[i] in self.dic['p']:
                    if self.top() in self.dic['p'][expresion[i]] :
                        print("posible reglas",self.dic['p'][expresion[i]][self.top()])
                        if len(self.dic['p'][expresion[i]][self.top()] ) > 1:
                            print("Hay mas de un posible camino")
                            if self.versions :
                                if self.dic['p'][expresion[i]][self.top()][1] != self.used():
                                    print("Probando otro camino en ",self.dic['p'][expresion[i]][self.top()][1])
                                    self.add(str(cont), 'p', expresion[i]+"_"+self.top()+'_'+self.dic['p'][expresion[i]][self.top()][1][1], self.dic['p'][expresion[i]][self.top()][1][1])

                                    self.estado = self.dic['p'][expresion[i]][self.top()][1][0]
                                    self.popPush(self.dic['p'][expresion[i]][self.top()][1][1])
                                    nTransiciones = nTransiciones + 1
                            else:
                                print('se creara una version par ',self.dic['p'][expresion[i]][self.top()][0])
                                newpila = self.pila.copy()
                                newestado = self.estado
                                newi = i
                                self.saveVersion(newi,newpila,newestado,self.dic['p'][expresion[i]][self.top()][0])
                                print('versions',self.versions)

                                print("Probando primer camino en ",self.dic['p'][expresion[i]][self.top()][0])
                                self.add(str(cont), 'p', expresion[i]+"_"+self.top()+'_'+self.dic['p'][expresion[i]][self.top()][0][1], self.dic['p'][expresion[i]][self.top()][0][1])

                                self.estado = self.dic['p'][expresion[i]][self.top()][0][0]
                                self.popPush(self.dic['p'][expresion[i]][self.top()][0][1])
                                nTransiciones = nTransiciones + 1
                            #endif
                        else:
                            print("Camino unico encontrado")
                            self.add(str(cont), 'p', expresion[i]+"_"+self.top()+'_'+self.dic['p'][expresion[i]][self.top()][0][1], self.dic['p'][expresion[i]][self.top()][0][1])
                            self.estado = self.dic['p'][expresion[i]][self.top()][0][0]
                            self.popPush(self.dic['p'][expresion[i]][self.top()][0][1])
                            nTransiciones = nTransiciones + 1
                        #endif
                    else:
                        print("No hay ruta para tope")
                        fin = True
                else:
                    print("No existe regla para la letara",expresion[i])
                    fin = True
                #endif
            elif self.estado == 'q':
                if expresion[i] in self.dic['q']:
                    if self.top() in self.dic['q'][expresion[i]] :
                        print("Camino uno encontrado en q")
                        self.add(str(cont), 'q', expresion[i]+"_"+self.top()+'_'+self.dic['q'][expresion[i]][self.top()][0][1], self.dic['q'][expresion[i]][self.top()][0][1])
                        self.estado = self.dic['q'][expresion[i]][self.top()][0][0]
                        self.popPush(self.dic['q'][expresion[i]][self.top()][0][1])
                        nTransiciones = nTransiciones + 1
                    else:
                        print("2-No hay ruta para tope")
                        fin = True
                else:
                    print("2-No existe regla para la letara",expresion[i])
                    fin = True
            #endif
            print("nTransiciones=",nTransiciones," cont=",cont)
            if nTransiciones == cont:
                if nTransiciones == len(expresion) and self.estado  != 'q' and self.versions and not fin:
                    print("Volveremos a un punto anterios")

                    # strPila = ''.join(self.versions[-1]['pila'])
                    # self.add(str(cont),self.versions[-1]['estado'],'',strPila)

                    self.estado = self.versions[-1]['estado']
                    self.setPila(self.versions[-1]['pila'])
                    i = self.versions[-1]['i']
                    cont = i
                    nTransiciones =  cont
                    self.verDatos(i,cont,nTransiciones)
                else:
                    i = i + 1   
            else:
                if self.versions and not fin :
                    print("Volveremos a un punto anterios")
                    
                    # strPila = ''.join(self.versions[-1]['pila'])
                    # self.add(str(cont),self.versions[-1]['estado'],'',strPila)

                    self.estado = self.versions[-1]['estado']
                    self.setPila(self.versions[-1]['pila'])
                    i = self.versions[-1]['i']
                    cont = i
                    nTransiciones =  cont
                    self.verDatos(i,cont, nTransiciones)
            if cont > len(expresion):
                break  
        #endwhile
        if self.top() == '#' and nTransiciones == len(expresion) :
            self.estado = 'r'

        if self.estado == 'r' :
            self.returnToInitialState()
            return {'isPalindrome':True, 'dataTable':self.dataTable}
        else:
            self.returnToInitialState()
            return {'isPalindrome':False, 'dataTable':self.dataTable}
