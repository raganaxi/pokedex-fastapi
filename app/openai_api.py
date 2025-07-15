# app/openai_api.py

import os
import httpx
import json

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4"  # o "gpt-3.5-turbo" si estás en pruebas

SYSTEM_PROMPT = """
Eres un asistente para formar equipos de Pokémon.

Responde siempre en formato JSON. Si el usuario quiere agregar un Pokémon al equipo, responde con una lista de acciones.

Ejemplo:
Usuario: ¿Muéstrame información de pikachu?
Respuesta:
{
  "action": "get_pokemon_by_name",
  "params": {
    "name": "pikachu"
  }
}
Usuario: Quiero ver los primeros pokémon
Respuesta:
{
  "action": "list_pokemon"
}

Usuario: Quiero agregar a Pikachu a mi equipo

Respuesta:
[
  {
    "action": "get_pokemon_by_name",
    "params": { "name": "pikachu" }
  },
  {
    "action": "add_to_team",
    "params": { "name": "pikachu" }
  }
]

Para ver el equipo actual:
{
  "action": "list_team"
}

Para reiniciar el equipo:
{
  "action": "reset_team"
}

Si no entiendes la intención del usuario, responde solo con:
{
  "reply": "No entendí tu mensaje, ¿puedes reformularlo?"
}
"""
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY no está definido en el entorno.")


async def get_action_from_message(message: str) -> list:
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": OPENAI_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ],
        "temperature": 0
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=body
        )
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]

        try:
            parsed = json.loads(content)
            if isinstance(parsed, dict):
                return [parsed]  # convertir a lista
            elif isinstance(parsed, list):
                return parsed
            else:
                return [{"reply": content}]
        except:
            return [{"reply": content}]

