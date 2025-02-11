#Escribe un programa que reciba una cadena de texto y la imprima al revés.
"""cadena = input("Escribe una cadena de texto: ")
cadena_invertida = cadena[::-1]  # Esto invierte la cadena
print(f"La cadena invertida es: {cadena_invertida}")"""

# Escribe un programa que reciba una cadena de texto y cuente cuántas veces
# aparece un carácter específico en esa cadena. El carácter debe ser proporcionado por el usuario.

"""word = input("Contaré cuantas veces aparece un caracter en una palabra, por favor ingresa tu palabra: ")
caracter_a_contar = input("¿Qué caracter deseas que cuente?: ")
word = word.lower()
contador = word.count(caracter_a_contar.lower())
print(f"El carácter '{caracter_a_contar}' aparece {contador} veces en la palabra.")"""

#Escribe un programa que reciba un número entero y lo imprima en orden inverso.
"""numero_entero = input("Por favor ingrese un numero entero: ")
# Verificamos si el número es negativo
if numero_entero[0] == '-':
    numero_invertido = '-' + numero_entero[:0:-1]  # Invertir el número y mantener el signo
else:
    numero_invertido = numero_entero[::-1]  # Solo invertir el número si es positivo

print(f"El número invertido es: {numero_invertido}")"""

# Escribe un programa que reciba un número y genere su tabla de multiplicar hasta el 10.
"""numero_multiplicar = int(input("Ingrese un numero y generare su tabla de multiplicar hasta el 10: "))
num = 1
while num < 10:
    resultado = numero_multiplicar * num
    print(f"{num} * {numero_multiplicar} = {resultado}")
    num += 1 """


def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active and touching_ghost:
        return "Bien hecho, puedes comer al fantasma"
    else:
        return "Cuidado!!, No puedes comer al fantasma"

print(eat_ghost(True,False))





