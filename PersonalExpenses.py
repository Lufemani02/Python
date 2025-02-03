print("Bienvenido a tu calculadora de gastos personales: ")

# Función para obtener valores numéricos
def get_number_input(mensaje):
    while True:
        try:
            return float(input(mensaje))  # Permite ingresar valores decimales
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número válido.")

# Solicitar ingresos y gastos con validación
income = get_number_input("Por favor, escribe tus ingresos mensuales: ")
outcome = get_number_input("Gracias, ahora ingresa tus gastos mensuales: ")

# Calcular balance
total = income - outcome

# Enlaces sugeridos
financial_tips_url = "https://www.coursera.org/specializations/investment-management"

# Evaluar balance y dar recomendaciones
if total < 0:
    print(f"Tienes un déficit de {-total} COP. Te recomiendo visitar: {financial_tips_url}")
elif total > 0:
    print(f"¡Enhorabuena! Estás ahorrando {total} COP al mes. 🎉")
else:
    print(f"Estás gastando todo lo que ganas. Revisa tus finanzas aquí: {financial_tips_url}")

print("Gracias por usar tu calculadora de gastos personales. ¡Hasta la próxima! 😊")