#Programa 2.2

SUE= float(input("Dame el valor de tu sueldo"))

if(SUE<1000):
    AUM= SUE*0.15
    NSUE= SUE+AUM
    print("Tu sueldo final es: ", NSUE)
