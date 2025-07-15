# app/routes.py

from fastapi import APIRouter, Request
from app.pokeapi import get_pokemon_by_name, list_pokemon
from app.openai_api import get_action_from_message
from app.memory import add_to_history, add_to_team, get_team, reset_team

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    steps = await get_action_from_message(message)

    final_reply = None

    for step in steps:
        if "reply" in step:
            final_reply = step["reply"]
            break

        action = step.get("action")
        params = step.get("params", {})

        if action == "get_pokemon_by_name":
            try:
                poke = await get_pokemon_by_name(params["name"])
                final_reply = f"{poke['name'].capitalize()} encontrado (ID {poke['id']})."
            except:
                final_reply = f"No encontré un Pokémon llamado {params.get('name', '')}."
                break

        elif action == "add_to_team":
            name = params.get("name")
            final_reply = add_to_team(name)

        elif action == "list_team":
            team = get_team()
            final_reply = (
                "Tu equipo está vacío." if not team
                else f"Tu equipo actual es: {', '.join(p.capitalize() for p in team)}"
            )

        elif action == "reset_team":
            reset_team()
            final_reply = "Tu equipo ha sido reiniciado."

        else:
            final_reply = "Acción desconocida."

    add_to_history(message, final_reply or "Sin respuesta")
    return {"reply": final_reply or "Sin respuesta"}
