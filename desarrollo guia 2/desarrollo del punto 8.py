edad=range(4,19)
edad_=range(19,110)
edadus=int(input("Ingrese la edad del cliente:"))
if edadus<4:
    print("La entrada es gratis.")
elif edadus in edad:
    print("Debe pagar $5.")
elif edadus in edad_:
    print("Debe pagar $10.")
else:
    print("No puede tener esa edad de acuerdo a la ciencia del 2024.") 