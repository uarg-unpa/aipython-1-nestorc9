lista=str(input("Ingrese una lista de caracteres: "))
lista=list(lista)         
vocales=["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
def vocal(list):
   return sum(c in vocales for c in list)
print("La cantidad de vocales que ingreso son: ", (vocal(lista)))