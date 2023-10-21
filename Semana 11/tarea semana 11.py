x = input("Ingrese una cadena de caracteres: ")

cant1 = 0
cant0 = 0
otro = 0

for i in x:
    if i == "1":
        cant1= cant1+1
    elif i == "0":
        cant0 = cant0+1
    else:
        otro = otro+1

print("Cantidad 0: "+ str(cant0))
print("Cantidad 1: " + str(cant1))
print("Otros Caracteres: "+ str(otro))