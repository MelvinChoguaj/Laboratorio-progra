class circulo():
    
    def __init__(self, radio):
        self.radio= radio

    def ob_perimetro(self):
        return (2*float(self.radio)*3.14)
            

    def ob_area(self):
        return (3.14*float(self.radio)**2)

    def ob_volumen(self):
        return ((4*3.14*(float(self.radio)**3))/3)

numcirculos=int(input("Ingrese la cantidad de circulos que desea: "))
circulos=[]

for i in range(numcirculos):
    print("Ingrese el radio del circulo "+ str(i+1))
    rad=float(input())
    circulos.append(rad)

for o in range(numcirculos):
    circulo1=circulo(circulos[o])

    print("El perimetro del circulo " + str(o+1)+ " es: " + str(circulo1.ob_perimetro()))
    print("El area del circulo " + str(o+1)+ " es: " + str(circulo1.ob_area()))
    print("El volumen del circulo " + str(o+1)+ " es: " + str(circulo1.ob_volumen()))
    print()