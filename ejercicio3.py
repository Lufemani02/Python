#Escribe un programa que determine si un número dado es primo o no.

numeritos = int(input("Escribe un número y te diré si es que este es primo: "))

if numeritos < 2:  # Los números menores que 2 no son primos
    print("Tu número no es primo")
else:
    es_primo = True
    for i in range(2, int(numeritos ** 0.5) + 1):  # Recorremos desde 2 hasta la raíz cuadrada de numeritos
        if numeritos % i == 0:  # Si es divisible por cualquier número, no es primo
            es_primo = False
            break
    if es_primo:
        print(f"El número {numeritos} es primo")
    else:
        print(f"El número {numeritos} no es primo")