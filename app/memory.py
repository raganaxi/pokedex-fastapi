# app/memory.py

from typing import List, Dict

history: List[Dict[str, str]] = []
current_team: List[str] = []  # nombres de Pokémon

def add_to_history(message: str, reply: str):
    history.append({"message": message, "reply": reply})

def get_history() -> List[Dict[str, str]]:
    return history[-10:]

def add_to_team(name: str) -> str:
    name = name.lower()
    if name in current_team:
        return f"{name.capitalize()} ya está en tu equipo."
    if len(current_team) >= 6:
        return "Tu equipo ya tiene 6 Pokémon."
    current_team.append(name)
    return f"{name.capitalize()} ha sido añadido a tu equipo. Llevas {len(current_team)}/6 Pokémon."

def get_team() -> List[str]:
    return current_team

def reset_team():
    current_team.clear()
