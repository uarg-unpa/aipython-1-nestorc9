a=int(input("Ingrese un número:"))
b=int(input("Ingrese un número:"))
c=int(input("Ingrese un número:"))
def numero(num):
    if a!= b and a!=c and b!=c:
        if a > b:
            if a > c:
                print("El numero mayor es: ", a)
            else:
                print("El numero mayor es: ", c)
        else:
            if b>c:
                print("El número mayor es:", b)
            else:
                print("El número mayor: ", c)
    else:
        print("Ingresa 3 numeros diferentes.")
numero(a)
