edad= int(input("Dame tu edad: "))
INE= bool(int(input("Tienes INE (0 No/ 1 Si): ")))

if edad>= 18 and INE== True:
    print("Es mayor de edad")
    print("puede entrar al Bar")
else:
    print("Eres menor de edad")
    print("Puedes ir a jugar LOL")
print("fin del programa")
