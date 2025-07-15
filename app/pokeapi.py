import httpx

BASE_URL = "https://pokeapi.co/api/v2"

async def get_pokemon_by_name(name: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BASE_URL}/pokemon/{name.lower()}")
        res.raise_for_status()
        return res.json()

async def list_pokemon(limit: int = 20):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BASE_URL}/pokemon?limit={limit}")
        res.raise_for_status()
        return res.json()
