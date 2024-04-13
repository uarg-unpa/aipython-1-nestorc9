n = int(input("Introduce un número entero positivo: "))
i=211
if n==1:
    print("1 no es primo.")
elif n==0:
    print("0 no es primo.")
elif n==2:
    print("2 es primo.")
else:
    while n % i != 0:
        i += 1
    if i == n:
        print(str(n) + " es primo")
    else:
        print(str(n) + " no es primo")