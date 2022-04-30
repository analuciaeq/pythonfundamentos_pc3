def ingreso_n(msg :str ="Ingrese la altura del triangulo de Pascal: ") -> int:
    try:
        n = int(input(msg))
        return n
    except:
        print('Ingrese bien el numero')
        return ingreso_n()

def main():
  
    altura = ingreso_n()
    print(f'la Potencia de {x} al cuadrado es : {potencia}')
    pass


try:
    main()
except:
    print('Hubo un fallo en el codigo')

