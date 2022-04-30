
class Rectangulo: 
    def __init__ (self, ancho, largo) -> None:
        self.ancho = ancho 
        self.largo = largo 
    def area (self):
        area = self.ancho * self.largo
        return area