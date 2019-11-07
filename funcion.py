def sumar(x,y):
    z=x+y
    return z

def restar(x,y):
    return x-y

def mi_print(texto):
    print(f"Este es mi print{tetxto}")

def multiplica (valor,veces):
    if veces==None:
        print("Debes enviar otro argumento")
    else:
        print(valor*veces)

def comanda(mesa,comensal,entrada,medio,fuerte,postre="gelatina de limon"): #argumentos de la funcion comanda
    print(f"Mesa {mesa} comensal{comensal}")
    print(f"\t entrada {entrada}") #t para sangria
    print(f"\t segundo tiempo {medio}")
    print(f"\t plato fuerte {fuerte}")
    print(f"\t postre {postre}")

def imprime_argumentos(*argumentos):
    for index in range (len (argumentos)):
        print(argumentos[index])

def comanda2( **comida ):
    llaves=comida.keys()
    for elem in llaves:
        print(elem,'-->',comida[elem])
    



a=10
b=5
c=sumar(a,b)
multiplica(10,3)
multiplica(10,None)
multiplica('hola',3)

print(f"La suma de {a} y {b} es {c}")
c=restar(a,b)
print(f"La resta de {a} y {b} es {c}")
comanda(2,1,"Ensalada","sopa","filete","flan") #cuando se mandan llamar los argumentoas se convierten en parametros
comanda("Ensalada","sopa","filete","flan",2,1)
comanda(entrada="Ensalada",medio="sopa",fuerte="filete",postre="flan",mesa=2,comensal=1)
comanda(entrada="Ensalada",medio="sopa",fuerte="filete",mesa=2,comensal=1)

imprime_argumentos('Hola',True,3.1416,1000,{'id':'sc01','nombre':'juan'})
imprime_argumentos()

comanda2(entrada="Ensalada",medio="sopa",fuerte="filete",mesa=2,comensal=1,postre="Strudel de manzana",bebida='coca ligth')
