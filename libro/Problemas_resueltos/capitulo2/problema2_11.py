CLAVE=int(input("Dame tu clave"))
NUMIN=float(input("Ingresa la duracion de la llamada"))

if CLAVE==12 or CLAVE==15 or CLAVE==18 or CLAVE==19 or CLAVE==23 or CLAVE==25 or CLAVE==29:
    if CLAVE==12:
        COST=NUMIN*2
        print("El costo de llamada total es ",COST)

    if CLAVE==15:
        COST=NUMIN*2.2
        print("El costo de llamada total es ",COST)

    if CLAVE==18:
        COST=NUMIN*4.5
        print("El costo de llamada total es ",COST)

    if CLAVE==19:
        COST=NUMIN*3.5
        print("El costo de llamada total es ",COST)

    if CLAVE==23 or CLAVE==25:
        COST=NUMIN*6
        print("El costo de llamada total es ",COST)

    if CLAVE==29:
        COST=NUMIN*5
        print("El costo de llamada total es ",COST)
else:
    print("No ingresaste un clave correcta")
