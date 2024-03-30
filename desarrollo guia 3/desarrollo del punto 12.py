n=int(input("Ingrese un numero natural:"))
b=0
for i in range(1,n+1):
    print(i, end="+")
    b=b+i
print("=", b)