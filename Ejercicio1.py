print("----------------------------------------")
print("Vector1: Lectura de N Elementos Enteros.")
print("----------------------------------------")
#inicializar
i = 1
F = [] #Inicializamos una Lista Vacia
#Entrada
print("Ingrese Nùmeros de elementos a Ingresar: ")
numElementos = int(input())
#Proceso
while i <= numElementos:
    elemento = int(input("Ingrese Elemento: "))
    F.append(elemento) #Agregar el elemento a la lista

    i = i + 1
#Salida
print("\nSALIDA")
print("----------------------------------------")
print(F)