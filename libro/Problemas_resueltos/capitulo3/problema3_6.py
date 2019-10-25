N=int(input("Ingresa la cantidad de numeros "))
i=0
M=-100000
ME=100000
while i<N:
    i+=1
    NUM=int(input("Ingresa un numero "))
    if NUM>M:
        M=NUM
        print("El numero mayor es ",NUM)
    elif NUM<ME:
        ME=NUM
        print("El numero menor es ",NUM)
print(f"El numero mayor es {M} y el menor es {ME}")


