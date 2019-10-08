CATE=int(input("Dame un numero entero"))
SUE=float(input("Dame la cantidad de tu sueldo actual"))
NSUE=0

if CATE==1:
    NSUE=SUE*1.15
elif CATE==2:
    NSUE=SUE*1.10
elif CATE==3:
    NSUE=SUE*1.08
elif CATE==4:
    NSUE=SUE*1.07
else:
    print(f"Tu categoria {CATE}no se encontro no tiene sueldo {NSUE} :c")

print(f"tu categoria es {CATE} y tu nuevo sueldo es {NSUE}")

