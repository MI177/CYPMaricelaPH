#ÁREA DE UN TRIÁNGULO CON FORMULA ESPECIFICA

L1=float(input("Dame el lado uno "))
L2=float(input("Dame el lado dos "))
L3=float(input("Dame el lado tres "))

S= (L1+L2+L3)/2
AREA= (S*(S-L1)*(S-L2)*(S-L3))**0.5

print("El área del triángulo es ",AREA)
