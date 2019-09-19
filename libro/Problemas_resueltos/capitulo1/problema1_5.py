#Progrma que calcula el área y volumen de un cilindro

RADIO = float(input("Dame el radio "))
ALTURA = float(input("Dame la altura "))

VOL= 3.141592*(RADIO**2)*ALTURA
ARE= 2*3.141592*RADIO*ALTURA

print(f"El volumen del cilindro es de {VOL} y el área es de {ARE}")
