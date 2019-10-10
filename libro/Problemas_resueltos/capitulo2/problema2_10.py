A=int(input("Dame un numero"))
B=int(input("Dame otrpo numero"))
C=int(input("Dame otrpo numero"))

if A>B:
    if A>C:
        print(f"{A} es el mayor")
    elif A==C:
        print(f"{C} Y {A} son iguales y son los mayores")

    else:
        print(f"{C} es el mayor")

elif A==B:
    if A>C:
        print(f"A y B son los mayores con valor {B}")
    elif A==C:
        print("Los mayores  e iguales son ",A,B,C)
    else:
        print("El mayor es ",C)
elif B>C:
    print("El mayor es ",B)
elif B==C:
    print(f"{B} y {C} son los mayores")
else:
    print("El mayor es ",C)

