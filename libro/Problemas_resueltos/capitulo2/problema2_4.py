#Programa 2.4

MAT=str(input("Ingrese el nombre de la materia "))
CAL1=float(input("Ingrese su calificacion "))
CAL2=float(input("Ingrese la siguiente calificacion "))
CAL3=float(input("Ingrese la siguiente calificacion "))
CAL4=float(input("Ingrese la siguiente calificacion "))
CAL5=float(input("Ingrese la siguiente calificacion "))
PRO=(CAL1+CAL2+CAL3+CAL4+CAL5)/5

if(PRO>=6):
    print(f"Esta aprobado en la materia de {MAT} y tu promedio es de {PRO}")
else:
    print(f"Esta reprobado en la materia de {MAT} y tu promedio es de {PRO}")

