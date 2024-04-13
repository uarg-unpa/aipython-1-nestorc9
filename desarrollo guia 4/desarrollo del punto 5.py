n=int(input("Ingrese un número: "))
def numero(num):
    if num % 2==0:
        print(f"El número {num} es par")
    else:
        print(f"El número {num} es impar")
numero(n)