#van entre llaves {} formato Jason 

alumno={'num_cta':'201647757473',
        'nombre':('Jose','Perez','Garcia'),
        
        'semestre':1,
        'promedio':0.0,
        'materia':['CYP','algebra','calculo','geometria','IntroICO'],
        'regular':True,
        'lagrimas':5,
        'direccion':{
                'calle':'Rancho Sequito',
                'colonia':'Impulsora Popular Avicola',
                'numero':1000,
                'cp':17570,
                'del_mun':'Nezahualcoyotl',
                'estado':{
                        'nombre':'Estado de Mexico',
                        'corto':'Edomex'
                }
        }
        }
print(alumno['nombre'])
print(alumno)
print(alumno['nombre'][1])
print(alumno['direccion']['cp'])
print(alumno['direccion']['estado']['corto'])
print(alumno['materia'][1].upper())
print(alumno['direccion']['estado']['nombre'][10::].upper())

alumno['lagrimas']=10
print(alumno)
#son mutables
alumno['cursa_ingles']=True
print(alumno)


mi_lista=[['a','b'],['c',10],['d',True]]
diccionario=dict(mi_lista)
print(diccionario)

#funcion keys()
llaves=alumno.keys()
print(llaves)
for llave in llaves:
    print("------------------------------------")
    print(llave)
    print("....................................")
    print(alumno[llave])
    print("++++++++++++++++++++++++++++++++++++")

#funcion values
for val in alumno.values():
    print('........')
    print(val)
    print('+++++++++++++++++++++++++')

#funcion items
for elem in alumno.items():
    print('........')
    print(elem)
    print('+++++++++++++++++++++++++')
