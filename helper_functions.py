import openai

# Configura tu API key de OpenAI
openai.api_key = 'tu_api_key_aqui'

def get_llm_response(prompt):
    """
    Función que consulta a la IA de OpenAI con un 'prompt' y devuelve la respuesta.
    """
    response = openai.chat_completions.create(
        model="gpt-3.5-turbo",  # Puedes usar cualquier modelo compatible, como "gpt-3.5-turbo" o "gpt-4"
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

def print_llm_response(response):
    """
    Función que imprime la respuesta de la IA.
    """
    print("Respuesta de la IA:", response)




