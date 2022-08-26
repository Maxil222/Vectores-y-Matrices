Suma = 0
Media = 0.0
C = 0
Temp = []
N = int(input())
for I in range (N):
    temperatura = float(input("Ingrese Temperatura {0} :".format(I + 1)))
    Temp.append(temperatura)
    Suma = Suma + Temp[I]
Media = Suma / N #Divisiòn Real

for tempElement in Temp:
    if tempElement >= Media:
        C = C + 1
    print(tempElement)


print("la media es: ",Media)
print("Total de Temperaturas >= a la media es ",C)
