print("Ejercicio 3: Jerarquia de operaciones")

print("¿Desea ingresar a la seleccion de operaciones?")
print("1: Si")
print("2: No")
sel=input()
sel=int(sel)
while sel<2:

    print("1: primera operacion")
    print("2: segunda operacion")
    print("3: tercera operacion")
    print("4: cuarta operacion")
    print("5: operacion cuadratica")
    print("6: Salir de las operaciones")
    op=input("Elija una de las opciones:")
    op=int(op)


    if op==1:
        
        x=input("Ingrese su primer numero")
        y=input("Ingrese su segundo numero")
        z=input("Ingrese su tercer numero")

        x=int(x)
        y=int(y)
        z=int(z)

        #primera operacion
        print(str(x)+"*"+str(y)+"+"+str(z)+"="+ str(x*y+z))

    elif op==2:
        x=input("Ingrese su primer numero")
        y=input("Ingrese su segundo numero")
        z=input("Ingrese su tercer numero")

        x=int(x)
        y=int(y)
        z=int(z)
        #segunda operacion
        print(str(x)+"*("+str(y)+"+"+str(z)+")="+ str(x*(y+z)))

    elif op==3:
        x=input("Ingrese su primer numero")
        y=input("Ingrese su segundo numero")
        z=input("Ingrese su tercer numero")

        x=int(x)
        y=int(y)
        z=int(z)
        #tercera operacion
        print(str(x)+"/("+str(y)+"*"+str(z)+")="+ str(x/(y*z)))

    elif op==4:
        x=input("Ingrese su primer numero")
        y=input("Ingrese su segundo numero")
        z=input("Ingrese su tercer numero")

        x=int(x)
        y=int(y)
        z=int(z)
        #cuarta operacion
        print("((3*"+str(x)+")+"+"(2*"+str(y)+"))/"+str(z)+"**2="+ str(((3*x)+(2*y))/z**2))

    elif op==5:
        x=input("Ingrese su primer numero")
        y=input("Ingrese su segundo numero")
        z=input("Ingrese su tercer numero")

        x=int(x)
        y=int(y)
        z=int(z)
        raiz2=(((y)**2)-4*x*z)
        #condiciones
        if x==0:
            print("ERROR: El primer numero(a) es igual a 0 y no se puede realizar la operacion")
    
        elif raiz2<0:
            print("ERROR: La raiz cuadrada no se puede realizar ya que es imaginaria")

        else:
            #operacion cuadratica
            print("x=(-"+str(y)+"+-((("+str(y)+")**2)-4*"+str(x)+"*"+ str(z)+")**0.5)/"+"2*"+str(x))
            raiz=(((y)**2)-4*x*z)**0.5
            print("x1="+str((-y+raiz)/(2*x)))
            print("x2="+str((-y-raiz)/(2*x)))
    
    elif op==6:
        print("Hasta pronto")
        break

    
    else:
        print("ERROR: La opcion seleccionada no esta definida")