NOM=0
print("Va a ingresar un sueldo? si su respuesta es no escriba -1")
SUE=float(input("Ingrese el sueldo "))

while(SUE!=-1):
    if(SUE<1000):
        NSUE=SUE*1.15
    else:
        NSUE=SUE*1.12

    NOM+=NSUE
    print("El nuevo sueldo es ", NSUE)
print("La nomina es ",NOM)

