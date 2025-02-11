#Escribe un programa que reciba una cadena de texto y cuente cuántas vocales (a, e, i, o, u) contiene.
cadena = input("Por favor ingresa un texto y te diré cuantas vocales tiene: ")
contador_vocales = 0

for letra in cadena.lower():  # Convierte la cadena a minúsculas para simplificar
    if letra in 'aeiou':  # Verifica si la letra es una vocal
        contador_vocales += 1

print(f"La cantidad de vocales es: {contador_vocales}")