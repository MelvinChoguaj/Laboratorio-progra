tablero1 = [["~" for _ in range(10)] for _ in range(10)]
tablero2 = [["~" for _ in range(10)] for _ in range(10)]


def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

while True:
    try:
        def colocar_barco(tablero1, fila, columna, tamaño, orientación):
            if orientación == "H":
                for i in range(tamaño):
                    if tablero1[fila][columna+i]=="~":
                        tablero1[fila][columna + i] = "B"
                    else:
                        print("Ya hay un barco en ese lugar")
                        raise ValueError
                    

            elif orientación == "V":
                for i in range(tamaño):
                    if tablero1[fila][columna+i]=="~":
                        tablero1[fila + i][columna] = "B"
                    else:
                        print("Ya hay un barco en ese lugar")
                        raise ValueError
            else:
                print("Orientación no válida")


        def disparo1(tablero1, fila, columna):
            if tablero1[fila][columna] == "B":
                tablero1[fila][columna] = "X" 
                print("Le diste a un barco") 
            
            elif tablero1[fila][columna] == "X":
                print("Ya hay un barco destruido")

            else:
                tablero1[fila][columna] = "O"  
                print("Disparo fallado")
                




        def colocar_barco(tablero2, fila, columna, tamaño, orientación):
            if orientación == "H":
                for i in range(tamaño):
                    if tablero2[fila][columna+i]=="~":
                        tablero2[fila][columna + i] = "B"
                    else:
                        print("Ya hay un barco en ese lugar")
                        raise ValueError
            elif orientación == "V":
                for i in range(tamaño):
                    if tablero2[fila][columna+i]=="~":
                        tablero2[fila + i][columna] = "B"
                    else:
                        print("Ya hay un barco en ese lugar")
                        raise ValueError
            else:
                print("Orientación no válida")

        def disparo2(tablero2, fila, columna):
            if tablero2[fila][columna] == "B":
                tablero2[fila][columna] = "X" 
                print("Le diste a un barco") 
            
            elif tablero2[fila][columna] == "X":
                print("Ya hay un barco destruido")
            else:
                tablero2[fila][columna] = "O"  
                print("Disparo fallado")

        def detectarga(tablero):
                for fila in tablero:
                    if "B" in fila:
                        return False
                return True
                
 

        
        for i in range (3):
            print("Turno del jugador 1 de colocar los barcos pequeños")
            colocar_barco(tablero1, int(input("Ingrese la fila en donde quiere colocar el barco pequeño "+ str(i+1)+" (0-9): ")), int(input("Ingrese la columna en donde quiere colocar el barco pequeño "+ str(i+1)+": ")), 3, input("Ingrese la orientacion del barco "+str(i+1)+", H para horizontal o V para vertical"))
            


        for i in range (2):
            print("Turno del jugador 1 de colocar los barcos grandes")
            colocar_barco(tablero1, int(input("Ingrese la fila en donde quiere colocar el barco grande "+ str(i+1)+" (0-9): ")), int(input("Ingrese la columna en donde quiere colocar el barco grande "+ str(i+1)+": ")), 5, input("Ingrese la orientacion del barco "+str(i+1)+", H para horizontal o V para vertical"))

        print("tablero 1")
        imprimir_tablero(tablero1)

        
        for i in range (3):
            print("Turno del jugador 2 de colocar los barcos pequeños")
            colocar_barco(tablero2, int(input("Ingrese la fila en donde quiere colocar el barco pequeño "+ str(i+1)+" (0-9): ")), int(input("Ingrese la columna en donde quiere colocar el barco pequeño "+ str(i+1)+": ")), 3, input("Ingrese la orientacion del barco "+str(i+1)+", H para horizontal o V para vertical"))

        for i in range (2):
            print("Turno del jugador 2 de colocar los barcos grandes")
            colocar_barco(tablero2, int(input("Ingrese la fila en donde quiere colocar el barco grande "+ str(i+1)+" (0-9): ")), int(input("Ingrese la columna en donde quiere colocar el barco grande "+ str(i+1)+": ")), 5, input("Ingrese la orientacion del barco "+str(i+1)+", H para horizontal o V para vertical"))

        print("tablero 2")
        imprimir_tablero(tablero2)
        break
    except (IndexError, ValueError):
        print("Cordenadas invalidas, vuelva a comenzar")
        tablero1 = [["~" for _ in range(10)] for _ in range(10)]
        tablero2 = [["~" for _ in range(10)] for _ in range(10)]




while True:

    print("turno jugador 1")
    disparo2(tablero2, int(input("Ingrese la fila en donde desea disparar")), int(input("Ingrese la columna en donde desea disparar")))
    print("turno jugador 2")
    disparo1(tablero1, int(input("Ingrese la fila en donde desea disparar")), int(input("Ingrese la columna en donde desea disparar")))
   
    
    if detectarga(tablero1):
        print("El jugador 2 ha ganado el juego")
        print("Felicitaciones!!")
        print("Asi quedaron los tableros")
        print("Tablero jugador 1")
        imprimir_tablero(tablero1)
        print("Tablero jugador 2")
        imprimir_tablero(tablero2)
        break

    elif detectarga(tablero2):
        print("El jugador 1 ha ganado el juego")
        print("Felicitaciones!!")
        print("Asi quedaron los tableros")
        print("Tablero 1")
        imprimir_tablero(tablero1)
        print("Tablero 2")
        imprimir_tablero(tablero2)
        break
    