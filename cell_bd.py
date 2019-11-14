

def leer_datos (path):
    file=open(path,'rt')
    lista_final=[]
    dic_cell={}
    datos=file.readlines()
    #print(datos)
    for ren in range (len(datos)):
        datos[ren]=datos[ren].strip().split(',')
    #print(datos)
    for ren in range (1,len(datos),1):
        dic_cell={}
        for col in range (len(datos[ren])):
            dic_cell[datos[0][col].strip()]=datos[ren][col]
        lista_final.append(dic_cell)
    #print(lista_final)
    return lista_final

def salida_formato(celular):
    print(f"celular marca {celular['marca']}")
    print(f"\t modelo {celular['modelo']}")
    print(f"\t almacenamiento {celular['almacenamiento']}")
    print(f"\t velocidad {celular['velocidad']}")
    print(f"\t RAM {celular['ram']}")
    print(f"\t color {celular['color']}")
    





def main():
    archivo= "celulares.txt"
    bd=leer_datos(archivo)
    print(f"DB={bd}")
    salida_formato(bd[6])

main()
