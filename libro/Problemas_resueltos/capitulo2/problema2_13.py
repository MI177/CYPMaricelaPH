MAT=int(input("Ingresa tu matricula "))
CARR=str(input("Ingresa el nombre de la carrera (contabilidad,economia,computacion,administracion) "))
SEM=int(input("Ingresa el semestre que estas cursando "))
PROM=float(input("Ingresa tu promedio actual "))

if CARR=="economia" or CARR=="computacion" or CARR=="contabilidad" or CARR=="administracion" or CARR=="economia":
    if SEM>=6 and PROM>=8.8:
        print(f"{MAT} tu carrera es {CARR} estas aceptado")
    elif CARR=="computacion":
        if SEM>6 and PROM>8.5:
                print(f"{MAT} tu carrera es {CARR} estas aceptado")
    elif CARR=="contabilidad" or CARR=="administracion":
        if SEM>5 and PROM>8.5:
                print(f"{MAT} tu carrera es {CARR} estas aceptado")
