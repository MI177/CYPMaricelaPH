

int(input("Ingresa un numero "))
PRO=0
PROT=0
C=0
i=0

while(i<N):
    i+=1
    NUM=int(input("Ingrese un numero "))
    if NUM>0:
        PRO+=NUM
        C+=1
    PROT+=NUM

print(f"El promedio de los numeros positivos es{PRO/C} y el de todos los numeros es {PROT/N}")

