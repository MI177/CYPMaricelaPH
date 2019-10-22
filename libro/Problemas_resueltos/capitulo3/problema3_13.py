ARSU=0
ARNO=0
MERSU=50000
ARCE=0
MES=0

for i in range (1,13,1):
    print(f" Mes {i}: ")
    RNO=int(input("Ingresa el promedio de lluvia del mes zona norte: "))
    RCE=int(input("Ingresa el promedio de lluvia del mes zona centro: "))
    RSU=int(input("Ingresa el promedio de lluvia del mes zona sur: "))

    ARNO=ARNO+RNO
    ARCE=ARCE+RCE
    ARSSU=ARSU+RSU

    if RSU<MERSU:
        MERSU=RSU
        MES=i

PRORCE=ARCE/12
print(f"Promedio region centro {PRORCE} el mes con menor lluvia en zona sur es {MES} y el registro del mes es {MERSU}")

if ARNO>ARCE:
    if ARNO>ARSU:
        print("La region con mayor lluvia es la norte")
    else:
        print("La region con mayor lluvia es la sur")
else:
    if ARCE>ARSU:
        print("La region con mayor lluvia es la centro")
    else:
        print("La region con mayot lluvia es la sur")
