
from time import clock_settime


def entrega_calificaciones(msg:str="Ingrese las calificaciones separadas por comas: ") -> int:
    try:
        calificaciones = input(msg)
        return calificaciones
    except:
        print('Ingrese correctamente los datos')
        return entrega_calificaciones()

def main():
    calificaciones = entrega_calificaciones()
    listafinal = calificaciones.split(sep=",")
    print (listafinal)
    pass

try:
    main()
except:
    print('Hubo un fallo en el codigo')
