    pila = ['#']
    estadoActual = 'p'
    dataTable = {}
 
    def add(self, index, state, rule):
        self.dataTable.setdefault(index,
            {
                "letter":"IDletter-"+index,
                "state":"IDstate-"+state,
                "rule":"ID"+rule
            }
        )

    def clean(self):
        self.dataTable = {}

    def top(self):
        return self.pila[-1]

    def popPush(self, apilar):
        self.pila.pop(-1)
        for l in apilar:
            if l != '' :
                self.pila.append(l)      

    def validar(self, expresion):
        nTransiciones = 0
        cont = 0
        # dv = DatosVista()
        self.dataTable = {}
        for w in expresion :
            cont = cont + 1
            if self.estadoActual == 'q':
                if w == 'b' and self.top() == 'b' :
                    self.popPush('')
                    nTransiciones =  nTransiciones + 1
                    print('b,b/', self.pila)
                    self.add(str(cont),'q','b-b-~')
                elif w == 'a' and self.top() == 'a' :
                    self.popPush('')
                    nTransiciones =  nTransiciones + 1
                    print('a,a/', self.pila)
                    self.add(str(cont),'q','a-a-~')
            elif self.estadoActual == 'p':
                if w == 'a' :
                    if self.top() == 'b' :
                        self.popPush('ba')
                        nTransiciones =  nTransiciones + 1
                        print('a,b/ba', self.pila)
                        self.add(str(cont),'p','a-b-ba')
                    elif self.top() == 'a' :
                        self.popPush('aa')
                        nTransiciones =  nTransiciones + 1
                        print('a,a/aa', self.pila)
                        self.add(str(cont),'p','a-a-aa')
                    elif self.top() == '#' :
                        self.popPush('#a')
                        nTransiciones =  nTransiciones + 1
                        print('a,#/#a', self.pila)
                        self.add(str(cont),'p','a-#-#a')
                elif w == 'b' :
                    if self.top() == 'b' :
                        self.popPush('bb')
                        nTransiciones =  nTransiciones + 1
                        print('b,b/bb', self.pila)
                        self.add(str(cont),'p','b-b-bb')
                    elif self.top() == 'a' :
                        self.popPush('ab')
                        nTransiciones =  nTransiciones + 1
                        print('b,a/ab', self.pila)
                        self.add(str(cont),'p','b-a-ab')
                    elif self.top() == '#' :
                        self.popPush('#b')
                        nTransiciones =  nTransiciones + 1
                        print('b,#/#b', self.pila)
                        self.add(str(cont),'p','b-#-#b')
                elif w == 'c' :
                    if self.top() == '#' :
                        self.popPush('#')
                        self.estadoActual = 'q'
                        nTransiciones =  nTransiciones + 1
                        print('c,#/#', self.pila)
                        self.add(str(cont),'p','c-#-#')
                    elif self.top() == 'b' :
                        self.popPush('b')
                        self.estadoActual = 'q'
                        nTransiciones =  nTransiciones + 1
                        print('c,b/b', self.pila)
                        self.add(str(cont),'p','c-b-b')
                    elif self.top() == 'a' :
                        self.popPush('a')
                        self.estadoActual = 'q'
                        nTransiciones =  nTransiciones + 1
                        print('c,a/a', self.pila)
                        self.add(str(cont),'p','c-a-a')
            
            if nTransiciones != cont : break
        #endfor
        if self.estadoActual == 'q' and self.top() == '#' and nTransiciones == len(expresion) :
            self.popPush('#')
            self.estadoActual = 'r'
            print(',#/#', self.pila)

        if self.estadoActual == 'r' : 
            self.returnToInitialState()
            return {'isPalindrome':True, 'dataTable':self.dataTable}
        else:
            self.returnToInitialState()
            return {'isPalindrome':False, 'dataTable':self.dataTable}
    
    def returnToInitialState(self):
        self.estadoActual = 'p'
        self.pila = ['#']