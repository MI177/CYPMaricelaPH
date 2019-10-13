TIPOENF=int(input("Ingrese el tipo de enfermedad del paciente "))
EDAD=int(input("Ingrese la edad del paciente "))
DIAS=int(input("Ingrese el numero de dias que el paciente estuvo hospitalizado "))

if TIPOENF==1 or TIPOENF==2 or TIPOENF==3 or TIPOENF==4:

    if TIPOENF==1:
        COSTOT=DIAS*25
    if TIPOENF==2:
        COSTOT=DIAS*16
    if TIPOENF==3:
        COSTOT=DIAS*20
    if TIPOENF==4:
        COSTOT=DIAS*32

elif EDAD>=14 or EDAD<=22:
    COSTOT=COSTOT*1.10

print("El costo total es ", COSTOT)
