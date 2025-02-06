#Funcion para eliminar los espacios en blanco que podría tener un String
def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

#Funcion para iterar e imprimir el texto de atras para adelante
def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves

# Ahora usamos dos funciones (No_space) y (Reverse) las cuales nos ayudan a verificar
# Si es que la palabra escrita es palindroma o no.
def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    # Usamos return para devolver el valor y comparar si es que nuestro String cumple con el objetivo.
    return texto == texto_al_reves

print(es_palindromo("amo la paloma"))
print(es_palindromo("Jeronimo y Sara"))