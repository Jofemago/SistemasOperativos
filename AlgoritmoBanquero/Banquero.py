from Proceso import Proceso


class Banquero:
    '''El banquero recibe,
        el numero de procesos aux[i] += aux[i] + p.getRecursoAsignado(i)a Ejecutar
        el numero de recursos
        una lista con los procesos
        una lista con ls estados de los recursos totales'''

    def __init__(self, nprocesos, nrecursos, listaprocesos, recursostotal):

        self.nprocesos_ = nprocesos
        self.nrecursos_ = nrecursos
        self.Procesos_ = listaprocesos
        self.RecursosTotal = recursostotal
        self.RecDips = [0]*self.nrecursos_ #recursos disponibles

        self.calcRecursosDisponibles()#calculo los recursos disponibles para inciar el proceso
        print('Estado Inicial')
        self.EstadoActual()
        self.iterar()



    def iterar(self):

        Finalizado = True
        iteraciones = 0
        while self.ValidaRecursos() and not self.isFinish():

            proceso = self.seleccionarProceso()
            if not proceso[0]:
                Finalizado = False
                print('no existe mas procesos')
                break
            p = proceso[1]
            print('iteracion Nro ', iteraciones)
            iteraciones += 1
            print('antes de ejecutar: ')
            self.Procesos_[p].MakeAsignacion() #asigno lo solicitado
            self.calcRecursosDisponibles() #recalculo disponibles
            self.EstadoActual()

            print('despues de ejecutar: ')
            self.Procesos_[p].EjecutarProceso() #asigno lo solicitado
            self.calcRecursosDisponibles() #recalculo disponibles
            self.EstadoActual()





        print('finalizado, se encontro respuesta: ', Finalizado)


    def seleccionarProceso(self):

        '''Con este metodo
            buscamos dentro de los procesos
            cual proceso requiere los recursos que estan
            libres en el momento,
            retonara si existe un proceso valido para ejecutra y el proceso indicado
            '''
        posible = True
        for p in range(self.nprocesos_):
            if not self.Procesos_[p].IsSolved():
                for r in range(self.nrecursos_):

                    if self.RecDips[r] < self.Procesos_[p].getRecursoSolicitado(r):

                        posible = False

                if posible:
                    return (True, p)
                posible = True

        return(False, None)

    def isFinish(self):
        '''valida si todos los procesos han sido finalizados '''

        for p in self.Procesos_:
            if not p.IsSolved():
                return False
        return True


    def ValidaRecursos(self):
        '''valida que existan recursos dispobibles ValidaRecursos
            si no hay recursos disponibles validos el algoritmo no peude continuar'''
        for e in self.RecDips:
            if e < 0:
                return False
        return True

    def EstadoActual(self):
        '''imprime el estado actual de todo el proceso'''
        print("\tSolicitados   Asignados")
        for p in self.Procesos_:
            print('\t',p.EstadoProceso())
        print("Total Recursos: ",self.RecursosTotal)
        print("Recursos Disponibles:",self.RecDips )
        print('\n')

    def calcRecursosDisponibles(self):
        '''calcula los recursos disponibles para el estado actual de los procesos'''
        aux = [0]*self.nrecursos_

        for p in self.Procesos_:
            #print(aux, "estado aux")
            #print(p.EstadoProceso())
            for i in range(self.nrecursos_):
                aux[i] = aux[i] + p.getRecursoAsignado(i)


        for i in range(self.nrecursos_):

            self.RecDips[i] = self.RecursosTotal[i] - aux[i]
