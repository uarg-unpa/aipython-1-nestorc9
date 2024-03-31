p=str(input("Ingrese una palabra: "))
def palabra(str):
    if str==str[::-1]:
        print("La palabra es un palíndromo.")
    else:
        print("La palabra no es un palíndromo.")
palabra(p)