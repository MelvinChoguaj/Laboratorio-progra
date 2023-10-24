class persona:
    def init(self):
        self.nombres=""
        self.apellidos=""
        self.casada=""
        self.nacimiento=""

    def in_nombres(self, nombres):
        self.nombres = nombres

    def in_apellidos(self, apellidos):
        self.apellidos = apellidos

    def apellido_casada(self, casada):
        self.casada = casada

    def in_fecha_nacimiento(self, nacimiento):
        self.nacimiento = nacimiento

    def ob_nombres(self):
        return self.nombres

    def ob_apellidos(self):
            return self.apellidos

    def ob_fecha_nacimiento(self):
        return str(self.nacimiento)
    
    def ob_nombre_completo(self):
        return (self.nombres) + (self.apellidos)
    
    def ob_casada(self):
        return str(self.casada)
    
persona1= persona()
persona1.in_nombres(input("Ingrese sus nombres: "))
persona1.in_apellidos(input("Ingrese sus apellidos: "))

persona1.apellido_casada(input("ingrese su apellido de casada, si no tiene dejelo en blanco: "))

persona1.in_fecha_nacimiento(input("ingrese su fecha de nacimiento: "))

print(persona1.ob_nombre_completo())
print(persona1.ob_casada())
print(persona1.ob_fecha_nacimiento())
