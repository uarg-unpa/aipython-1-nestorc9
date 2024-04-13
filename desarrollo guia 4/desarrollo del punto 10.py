def convertir(f):
    c=(f-32)*5/9
    return c
f=float(input("Ingrese los grados Fahrenheit: "))
print(f"Su valor en grados Celsius es:{convertir(f)}")