import random

# Función para crear un tablero vacío
def crear_tablero():
    tablero = [[' ' for _ in range(10)] for _ in range(10)]
    return tablero

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    print("  1 2 3 4 5 6 7 8 9 10")
    letras = "ABCDEFGHIJ"
    for i in range(10):
        fila = ' '.join(tablero[i])
        print(f"{letras[i]} {fila}")

# Función para colocar barcos en el tablero
def colocar_barco(tablero, fila, columna, orientacion, longitud):
    if orientacion == "horizontal":
        for i in range(longitud):
            tablero[fila][columna + i] = 'O'
    else:
        for i in range(longitud):
            tablero[fila + i][columna] = 'O'

# Función para verificar si un disparo ha alcanzado un barco
def disparo(tablero, fila, columna):
    if tablero[fila][columna] == 'O':
        tablero[fila][columna] = 'X'  # 'X' representa un barco golpeado
        return True
    else:
        tablero[fila][columna] = '-'  # '-' representa un disparo fallido
        return False

# Función para determinar si un jugador ha ganado
def jugador_ganador(tablero):
    for fila in tablero:
        if 'O' in fila:
            return False
    return True

# Inicializar los tableros de juego para ambos jugadores
tablero_jugador1 = crear_tablero()
tablero_jugador2 = crear_tablero()

# Colocar barcos en el tablero para cada jugador
# Esto es solo un ejemplo, puedes personalizar la ubicación de los barcos
colocar_barco(tablero_jugador1, 0, 0, "horizontal", 3)
colocar_barco(tablero_jugador1, 1, 3, "vertical", 5)
colocar_barco(tablero_jugador2, 2, 2, "horizontal", 3)
colocar_barco(tablero_jugador2, 4, 7, "vertical", 5)

# Juego
turno = 1
while True:
    if turno == 1:
        print("Turno del Jugador 1")
        imprimir_tablero(tablero_jugador1)
        fila, columna = input("Elige una casilla para disparar (por ejemplo, A2): ").upper(), int(input())
        fila = ord(fila[0]) - ord('A')
        columna -= 1
        if disparo(tablero_jugador2, fila, columna):
            print("¡Tocado!")
        else:
            print("Agua")
        if jugador_ganador(tablero_jugador2):
            print("¡Jugador 1 gana!")
            break
        turno = 2
    else:
        print("Turno del Jugador 2")
        imprimir_tablero(tablero_jugador2)
        fila, columna = input("Elige una casilla para disparar (por ejemplo, B3): ").upper(), int(input())
        fila = ord(fila[0]) - ord('A')
        columna -= 1
        if disparo(tablero_jugador1, fila, columna):
            print("¡Tocado!")
        else:
            print("Agua")
        if jugador_ganador(tablero_jugador1):
            print("¡Jugador 2 gana!")
            break
        turno = 1