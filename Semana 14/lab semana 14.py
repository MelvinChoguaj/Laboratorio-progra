class automovil():
    def __init__(self):
        self.modelo=2024
        self.precio=200000.00
        self.marca="Toyota"
        self.disponible=True
        self.tipodecambio=7.89
        self.descuento=0.15
    
    def defmodelo(self, modelo):
        self.modelo=int(modelo)

    def defprecio(self, precio):
        self.precio=float(precio)    

    def defmarca(self,marca):
        self.marca=marca
    
    def deftipcambio(self, tipodecambio):
        self.tipodecambio=float(tipodecambio)
    
    def defdisp(self, disponible):
        self.disponible=bool(disponible)
    
    def cambio(self):
        return (self.precio*self.tipodecambio)

    def cambdis(self):
        if self.disponible== True:
            self.disponible=False
        elif self.disponible==False:
            self.disponible=True
    
    def mostrardisp(self):
        
        if self.disponible== True:
            print("Disponible")
        elif self.disponible==False:
            print("No se encuentra disponible actualmente")
    
    def aplicdes(self):
        return (self.precio*self.descuento)
        
    def mostrarinf(self):
        print("Marca: "+ str(self.marca)+ ", Modelo: "+ str(self.modelo)+ ", Precio de venta: "+ str(self.precio)+ ", Precio en dolares"+ str(automovil.cambio))
        print(automovil.mostrardisp)



