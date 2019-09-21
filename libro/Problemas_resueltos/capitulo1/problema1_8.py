#Programa que calcula la distancia entre dos puntos

X1= float(input("Dame el valor de x1 "))
Y1= float(input("Dame el valor de y1 "))
X2= float(input("Dame el valor de x2 "))
Y2= float(input("Dame el valor de y2 "))

DIS= ((X1-X2)**2+(Y1-Y2)**2)**0.5

print("La distancia entre los puntos dados es ",DIS)
