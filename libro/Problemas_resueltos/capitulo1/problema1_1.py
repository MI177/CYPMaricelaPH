#Programa que da cambio

PREPRO = float(input("Dame el precio del producto  "))
PAGO = float(input("Dame el valor del pago  "))

DEVO = PAGO - PREPRO

print(f"Pagaste ${PAGO}  y el precio del prod es: ${PREPRO} y tu cambio es ${DEVO}")

