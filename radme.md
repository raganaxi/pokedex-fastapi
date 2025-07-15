# 🧠 Pokedex FastAPI Chatbot (MCP Example)

Este es un proyecto de ejemplo para construir un chatbot estilo MCP (Model-Context-Protocol) utilizando:

- **FastAPI** como servidor backend
- **OpenAI API** para interpretación del lenguaje natural
- **PokeAPI** para datos reales de Pokémon
- **Docker** para el entorno aislado
- **Makefile** para tareas automatizadas

---

## 🚀 Requisitos

- Docker y Docker Compose
- Make

---

## ⚙️ Primeros pasos

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/pokedex-fastapi.git
cd pokedex-fastapi
```

2. Inicializa tu archivo de entorno:

```bash
make init
```

Esto copia `.env.example` a `.env`.

3. Edita tu archivo `.env` y asegúrate de definir:

```env
APP_PORT=3001
OPENAI_API_KEY=sk-xxx...
```

4. Verifica las variables:

```bash
make check-env
```

5. Construye el proyecto:

```bash
make build
```

6. Levanta el servidor:

```bash
make up
```

El backend estará disponible en: [http://localhost:3001](http://localhost:3001)

---

## 💬 Ejemplo de uso del chat

Endpoint: `POST /chat`

Body de ejemplo:

```json
{ "message": "Quiero agregar a Pikachu a mi equipo" }
```

Respuesta esperada:

```json
{ "reply": "Pikachu ha sido añadido a tu equipo. Llevas 1/6 Pokémon." }
```

---

## 🛠️ Comandos útiles

```bash
make init        # Copia .env.example a .env si no existe
make check-env   # Verifica APP_PORT y OPENAI_API_KEY
make build       # Construye los contenedores Docker
make up          # Inicia el proyecto
make down        # Detiene los contenedores
make restart     # Reinicia el servidor
make logs        # Muestra logs en tiempo real
make sh          # Abre una shell en el contenedor web
make port        # Muestra el puerto actual configurado
make ps          # Muestra el estado de los contenedores
make clean       # Borra los volúmenes (limpieza total)
make test-env    # Muestra todas las variables cargadas (oculta valores)
```

---

## 📚 Arquitectura

Este proyecto sigue el patrón MCP: el modelo interpreta, planea y actúa paso a paso.

Ejemplo de respuesta de OpenAI:

```json
[
  { "action": "get_pokemon_by_name", "params": { "name": "pikachu" } },
  { "action": "add_to_team", "params": { "name": "pikachu" } }
]
```

---

## 🧪 Endpoint de prueba

Puedes hacer pruebas con herramientas como [Postman](https://www.postman.com/) o `curl`:

```bash
curl -X POST http://localhost:3001/chat \
     -H "Content-Type: application/json" \
     -d '{ "message": "agrega a bulbasaur" }'
```

---

## 🧹 Licencia MIT

