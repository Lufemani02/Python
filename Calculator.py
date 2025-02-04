#Menu para darle la bienvenida al usuario
print("Bienvenido a la calculadora \nPara salir, escribe Salir")
print("Las operaciones son: Suma(+), Resta(-), Multiplicacion(*), Division(/)")

# Variable global para ir almacenando los resultados
resultado = ""
while True:
    if not resultado:
        resultado = input("Por favor ingrese su primer numero: ")
        # Validacion para que el usuario pueda salir del sistema si asi lo desea
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    operacion = input("Ingrese la operacion que desea ejecutar: ")
    # Validacion para que el usuario pueda salir del sistema si asi lo desea
    if operacion.lower() == "salir":
        break
    num2 = input("Gracias, ahora ingresa otro numero: ")
    # Validacion para que el usuario pueda salir del sistema si asi lo desea
    if num2.lower() == "salir":
        break
    # Validacion de la operacion que el usuario desea ejecutar
    if operacion.lower() == "Suma" or operacion == "+":
        resultado += int(num2)
        print(f"El resultado es: {resultado}")
    elif operacion.lower() == "Resta" or operacion == "-":
        resultado -= int(num2)
        print(f"El resultado es: {resultado}")
    elif operacion.lower() == "Multiplicacion" or operacion == "*":
        resultado *= int(num2)
        print(f"El resultado es: {resultado}")
    elif operacion.lower() == "Division" or operacion == "/":
        resultado /= int(num2)
        print(f"El resultado es: {resultado}")
    else:
        print("Opcion no valida")
        break
#