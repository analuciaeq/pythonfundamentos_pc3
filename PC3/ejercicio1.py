
from operator import truediv


def calcular_longitud (mensaje:str)->int:
    
    palabras = mensaje.split(sep=" ")
    while True:
        if palabras[-1] == ' ':
            palabras.pop()
        else:
            break
    longitud = len(palabras[-1])
    return longitud

