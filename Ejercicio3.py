Vec = []
print("Ingrese numeros de elementos del vector")
N = int(input())
if 1<=N and 1<=200:
    for i in range (1,N+1):
        print("ingrese valor ", i)
        elemento = int(input("Ingrese Entero {0}: ".format(i)))
        Vec.append(elemento)
        print("Lista de numeros sin repeticiones")
else:
    print("El numero de elementos del vector es incorrecto")
