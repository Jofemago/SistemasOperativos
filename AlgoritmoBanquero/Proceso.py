

class Proceso:

    def __init__(self,NroRecursos, lista):

        self.recursos = NroRecursos
        self.Asignados = self.makeAsignados(lista)
        self.Solicitados = self.MakeSolicitados(lista)



    #--------------------------------------------------------------------------
    #metodos geters y setters para obtener o modificar la cantidad solicitada o asginada

    def getRecursoAsignado(self, i):

        assert i < self.recursos
        return self.Asignados[i]

    def getRecursoSolicitado(self, i):

        assert i < self.recursos
        return self.Solicitados[i]


    def setRecursoAsignado(self, i, recurso):

        assert i < self.recursos
        self.Asignados[i] = recurso

    def setRecursoSolicitado(self, i,recurso):

        assert i < self.recursos
        self.Solicitados[i] = recurso


    #--------------------------------------------------------------------------
    def IsSolved(self):
        '''retorna True si el proceso ya ha sido ejecutado
            False si el proceso tiene recurso asignado o tiene esta solicitando '''

        res = 0
        for i in self.Asignados:
            res += i
        for i in self.Solicitados:
            res += i

        return res == 0

    def MakeAsignacion(self):

        '''si el banquero lo requiere se asignara lo solicitado'''
        for i in range(self.recursos):

            self.Asignados[i] = self.Asignados[i] + self.Solicitados[i]

    def EjecutarProceso(self):

        "ejecuta el proceso"
        for i in range(self.recursos):
            self.Asignados[i] = 0
            self.Solicitados[i] = 0




    def EstadoProceso(self):
        '''devuelve una cadena que se encarga de mostrar primero los recursos solicitados
            y luego los recursos asignados'''
        res = ""
        for i in self.Solicitados:

            res += str(i)+ " "

        res+= "   "
        for i in self.Asignados:

            res += str(i)+ " "

        return res


    #Metodos para cargar listas de asignados y solicitados
    def makeAsignados(self, lista):

        l = []
        for i in range(self.recursos):
            l.append(int( lista[i]))
        return l


    def MakeSolicitados(self, lista):

        l = []
        for i in range(self.recursos, self.recursos * 2):
            l.append(int( lista[i]))
        return l
