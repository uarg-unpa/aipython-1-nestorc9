contraseña_guardada="hola python"
contraseña_introducida=str(input("Ingrese una contraseña:"))
if contraseña_guardada == contraseña_introducida:
    print("Acceso correcto.")
elif contraseña_guardada==(contraseña_introducida.lower()):
    print("Acceso correcto.")
elif contraseña_guardada==(contraseña_introducida.upper()):
    print("Acceso correcto.")
else:
    print("Acceso denegado.")