CUECER=0
N=int(input("Dame un numero entero "))

for I in range(0,N,1):
    NUM=int(input("Ingresa un entero "))

    if NUM==0:
        CUECER+=1
print("El numero de ceros es ",CUECER)


