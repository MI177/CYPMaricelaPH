

NUM=int(input("Ingrese un numero entero positivo "))
while(NUM!=1):
    if NUM%2==0:
        NUM/=2
    else:
        NUM=(NUM*3)+1
    print(NUM)
