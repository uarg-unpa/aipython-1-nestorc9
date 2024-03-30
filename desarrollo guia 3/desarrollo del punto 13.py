n=int(input("Ingrese un número natural: "))
b=0
for i in range(2,n+1,2):
    print(i, end="+")
    b=b+i
print("=", b)