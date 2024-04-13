num=int(input("Ingrese un número entero positivo mayor a tres: "))
if num<3:
    print("Ingrese un número mayor a tres.")
else:
    for i in range(1, num+1, 2):
        print(i, end=",")