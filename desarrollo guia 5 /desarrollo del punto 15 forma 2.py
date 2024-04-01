print("Ingrese 0 cuando desee dejar de ingresar números.")
def prom():
    nume=[]
    while True: 
        num=int(input("Ingrese numeros enteros positivos: "))
        
        if num==0:
            break
        else:
            nume.append(num)
    po=0
    for i in nume:
        po+=i
    average=po/len(nume)
    print("Tu promedio es de:",average) 
    print(nume)
    return(prom)
prom()