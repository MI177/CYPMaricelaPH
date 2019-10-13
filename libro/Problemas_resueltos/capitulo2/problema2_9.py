PREBAS=float(input("Ingresa el precio del articulo "))

if PREBAS>500:
    IMP=20*0.30+(PREBAS-40)*0.5

elif PREBAS>40:
    IMP=20*0.30+(PREBAS-40)*0.40

elif PREBAS>20:
    IMP=(PREBAS-20)*0.30

else:
    IMP=0

PRETOT=PREBAS+IMP

print(f"El costo real del producto es {PRETOT} y el valor del producto sin impuestos es {PREBAS}")

