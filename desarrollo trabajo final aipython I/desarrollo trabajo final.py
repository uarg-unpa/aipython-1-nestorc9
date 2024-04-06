import random;
lista=[]
lista1=[]
def lanzar_dado():
    res= input("Quiere tirar los dados:")
    res= res.lower()
    while(res=="si" or res=="s"):
        d1=random.randint(1,6)
        d2=random.randint(1,6)
        print("El dado uno cayo en", str(d1), "y el dado dos cayo en", str(d2),".")
        lista.append(d1)
        lista1.append(d2)    
        res= input("Desea jugar de vuelta:")
        res= res.lower()
lanzar_dado()
print(f"Los resultados obtenidos del Jugador 1 son:{lista}")
print(f"Los resultados obtenidos del Jugador 2 son:{lista1}")
   