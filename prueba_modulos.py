import Modulos

Modulos.mi_print("Hola")

from Modulos import mi_print, otro_print,sumar,restar #Administracion de codigos
#from modulos import * para importar todos en lugar de uno por uno 
import time
import sys
from asciistuff import Banner 


mi_print("Hola de nuevo")

otro_print("otro print usado")
print(sumar(4,5))
print(restar(10,7))

for i in range (10,0,-1):
    print(i,"...")
    time.sleep(.25)

print(sys.platform)
print(Banner("BOOM"))
