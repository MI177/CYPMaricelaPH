i=0
MED=0
CHI=0
GRA=0
V=int(input("Ingresa la cantidad de ventas "))

while i<V:
    i+=1
    VENT=float(input("Numero de ventas "))
    if VENT<200:
        MED+=1
    elif VENT>200 and VENT<400:
        CHI+=1
    else:
        GRA+=1
print(CHI,MED,GRA)

