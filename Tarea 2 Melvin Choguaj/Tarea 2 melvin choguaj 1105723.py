class   Clase:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def primer_numero(self, num):
        self.num1 = num

    def segundo_numero(self, num):
        self.num2 = num

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: No se puede dividir por cero"


clase1 = Clase()

while True:
    print("Menu:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Selecciona una opcion: ")
    opcion=int(opcion)

    if opcion == 1:
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        clase1.primer_numero(num1)
        clase1.segundo_numero(num2)
        print("La suma es:", clase1.suma())
    elif opcion == 2:
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        clase1.primer_numero(num1)
        clase1.segundo_numero(num2)
        print("La resta es:", clase1.resta())
    elif opcion == 3:
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        clase1.primer_numero(num1)
        clase1.segundo_numero(num2)
        print("La multiplicacion es:", clase1.multiplicacion())
    elif opcion == 4:
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        clase1.primer_numero(num1)
        clase1.segundo_numero(num2)
        resultado = clase1.division()
        print("La division es:", resultado)
    elif opcion == 5:
        print("Adios")
        break
    else:
        print("ERROR. La opcion seleccionada no existe")
