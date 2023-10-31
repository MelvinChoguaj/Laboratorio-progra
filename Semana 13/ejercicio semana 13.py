class circulo():
    
    def __init__(self, radio):
        self.radio= radio

    def ob_perimetro(self):
        return (2*float(self.radio)*3.14)
            

    def ob_area(self):
        return (3.14*float(self.radio)**2)

    def ob_volumen(self):
        return ((4*3.14*(float(self.radio)**3))/3)

circulo1=circulo(5)

print("El perimetro del circulo es: " + str(circulo1.ob_perimetro()))
print("El area del circulo es: " + str(circulo1.ob_area()))
print("El volumen del circulo es: " + str(circulo1.ob_volumen()))