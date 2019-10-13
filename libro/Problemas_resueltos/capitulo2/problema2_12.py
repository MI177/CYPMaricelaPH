SUE=float(input("Ingresa el valor de tu sueldo actual "))
CATE=int(input("Ingresa tu categoria entre 1 y 8 "))
HE=int(input("Ingresa las horas extra que trabajas "))

if CATE==1 or CATE==2 or CATE==3 or CATE==4:
    if CATE==1:
        PHE=30
    elif CATE==2:
        PHE=38
    elif CATE==3:
        PHE=50
    elif CATE==4:
        PHE=70
else:
    PHE=0

if HE>30:
    NSUE=SUE+30*PHE
else:
    NSUE=SUE+HE*PHE

print("Tu nuevo sueldo es ",NSUE)
