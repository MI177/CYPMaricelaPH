#Programa 2.3, programa que calcula las raices

A=float(input("Dame el valor de la primera variable"))
B=float(input("Dame el valor de la segunda variable"))
C=float(input("Dame el valor de la tercera variable"))
DIS=B**2-4*A*C

if(DIS>0):
    X1=((-B)+DIS**0.5)/2*A
    X2=((-B)-DIS**0.5)/2*A
    print("Las raices reales son ", X1, X2,)
