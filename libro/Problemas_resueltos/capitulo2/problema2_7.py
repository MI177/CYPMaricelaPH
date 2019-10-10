A=int(input("Dame un numero entero"))
B=int(input("Dame otro numero"))
C=int(input("Dame otro numero"))

if A<B:
    if B<C:
        print("Los numero estan en orden creciente")
    else:
        print("Los numeros no estan en orden creciente")
else:
    print("Los numeros no estan en orden creciente")
