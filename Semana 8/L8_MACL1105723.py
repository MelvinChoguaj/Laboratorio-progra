while True:
    print("")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")
    op=input("Seleccione una de las opciones")
    op=int(op)

    if op==1:
        num=input("Ingrese un numero")
        num=int(num)
        fact=1
        fact=int(fact)

        for i in range(1, num+1):
            fact=fact*i
        print(str(num)+"*...*2*1="+str(fact))

    elif op==2:  
        x=0
        y=1
        z=0

        v1=input("Ingrese un numero")
        v1=int(v1)

        print(str(x)+","+str(y)+",",end="")

        for l in range(0, v1):
            z=x+y
        
            print(str(z)+",",end="")
            x=y
            y=z
        print("Fibonacci("+str(v1)+")")
        
    elif op==3:
        break

    else:
        print("ERROR, El numero seleccionado no esta entre las opciones")