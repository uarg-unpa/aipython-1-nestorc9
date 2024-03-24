si=18
paga=100000
edadus=int(input("Ingrese su edad:"))
salarious=int(input("Ingrese su salario:$"))
if edadus > si and salarious>=paga:
    print("Usted debe pagar el impuesto ya que es mayor de edad y supera los $100000 de salario mensual.")
else:
    print("Usted no debe pagar el impuesto ya que no es mayor de edad o no supera los $100000 de salario mensual")