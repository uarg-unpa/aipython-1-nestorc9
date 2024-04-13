num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero:"))
if num1>=num2:
    print("El segundo número debe ser mayor que el primero.")
else:
    while num1<=num2:
        print(num1)
        num1+=1