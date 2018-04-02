from Proceso import Proceso
from Banquero import Banquero
import sys




if __name__ == '__main__':

    if (len(sys.argv) > 1):
        trabajo = sys.argv[1]
    else:
        trabajo = './ejemplos/prueba.txt'

    f = open(trabajo,'r')
    lista = f.readlines()
    Nrorecursos = int( lista[0])
    Nroprocesos = int( lista[1])


    #creo una lista con todos los procesos a ejeceutar
    Procesos = []
    for i in range(2, Nroprocesos + 2):

        k = lista[i].split(" ")
        Procesos.append(Proceso(Nrorecursos, k))

    '''for p in Procesos:
        print(p.EstadoProceso())'''

    #obtenemos todos los recursos Disponibles
    RecursosDisponibles = []
    for e in lista[len(lista) - 1].split(" "):

        RecursosDisponibles.append(int(e))

    banquero = Banquero(Nroprocesos, Nrorecursos, Procesos,RecursosDisponibles)
