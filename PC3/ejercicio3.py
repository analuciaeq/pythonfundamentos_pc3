import math
class Circulo:
    def __init__ (self, radio) -> None:
        self.radio = radio 
    def area (self):
        circulo = self.radio * self.radio * math.pi
        return(circulo) 

