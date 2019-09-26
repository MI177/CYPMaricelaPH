#Programa 2.4

SUE = float(input("Ingresa tu sueldo "))

if(SUE<1000):
    NSUE= SUE*1.15
    print("Tu sueldo final es de: ",NSUE)
else:
    NSUE= SUE*1.12
    print("Tu sueldo final es de: ",NSUE)
