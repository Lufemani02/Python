# Función para obtener los granos en la casilla number
def square(number):
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)
# Total de granos en el tablero
def total():
    return 2**64 - 1
try:
    number = 10  # Aquí puedes cambiar el valor de n para probar otros casos
    print(f"En la casilla {number} hay {square(number)} granos.")
except ValueError as e:
    print(f"Error: {e}")
print(f"El total de granos en el tablero es {total()}.")