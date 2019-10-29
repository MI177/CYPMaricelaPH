#Arreglos
#Lectura
#Escritura/asignacion
#Actualizacion:insercion, eliminacion, modificacion
#Ordenamiento
#Busqueda

frutas= ["Zapote","Manzana", "Pera", "Aguacate", "Durazno","Uva", "Sandia"] #Escritura

#Lectura, selector [indice]
print(frutas[2])

#Lectura con for
#opcion 1
print("------------------------------------")
for indice in range (0,7,1):
    print(frutas[indice])

print("------------------------------------")
#for opcipon 2 por un iterador for each

for fr in frutas:
    print(fr)

print("------------------------------------")
#Asignacion
frutas [2]="Melon"
print(frutas)

print("------------------------------------")
#Insercion al final dir(tipo de dato) help(tipo de dato.insert)
frutas.append("Naranja")
print(frutas)
print(len(frutas))

frutas.insert(2,"Limon")
print(frutas)
print(len(frutas))

frutas.insert(0, "Mamey")
print(frutas)

print("------------------------------------")
#Eliminicacion remove y pop

print(frutas.pop())
print(frutas)

print(frutas.pop(1))
print(frutas)

frutas.append("Limon")
frutas.append("Limon")
print(frutas)
frutas.remove("Limon")
print(frutas)

print("------------------------------------")
#Ordenamiento

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

print("------------------------------------")
#Busqueda

print(f"El Uva esta en la posicion {frutas.index('Uva')}")
print(f"El Limon esta {frutas.count('Limon')} en la lista")

print("------------------------------------")
#Extend Concatenar

print(frutas)
otras_frutas=["Rambutan", "Nispero","Liche","Pitaya"]

frutas.extend(otras_frutas)
print(frutas)

print("------------------------------------")
#Copiar

copia=frutas
copia.append("Naranja")
print(frutas)
print(copia)

otra_copia=frutas.copy()
otra_copia.append("Fresa")
otra_copia.append("Fresa")
print(frutas)
print(otra_copia)








































