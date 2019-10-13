#Problema 2.8 pag 89

COMPRA=float(input("Dame el valor de total de tu compra "))

if COMPRA<500:
    PAGAR=COMPRA
    print("El valor a pagar es ", PAGAR)

elif COMPRA<=1000:
    PAGAR=COMPRA-(COMPRA*0.05)
    print("El valor a pagar es ", PAGAR)

elif COMPRA<=7000:
    PAGAR=COMPRA-(COMPRA*0.11)
    print("El valor a pagar es ", PAGAR)

elif COMPRA<=15000:
    PAGAR=COMPRA-(COMPRA*0.18)
    print("El valor a pagar es ", PAGAR)

else:
    PAGAR=COMPRA-(COMPRA*0.25)
    print("El valor a pagar es ", PAGAR)
