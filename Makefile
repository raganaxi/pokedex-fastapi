# Makefile para pokedex-fastapi

ENV_FILE := .env
EXAMPLE_ENV := .env.example
DOCKER_COMPOSE = docker compose

init:
	@if [ ! -f $(ENV_FILE) ]; then \
		echo "Copiando $(EXAMPLE_ENV) a $(ENV_FILE)"; \
		cp $(EXAMPLE_ENV) $(ENV_FILE); \
	else \
		echo "$(ENV_FILE) ya existe"; \
	fi

check-env:
	@echo "🔍 Verificando variables de entorno..."
	@if [ ! -f $(ENV_FILE) ]; then \
		echo "❌ Archivo .env no encontrado. Ejecuta 'make init' primero."; \
		exit 1; \
	fi

	@if ! grep -q "^APP_PORT=" $(ENV_FILE); then \
		echo "❌ Falta APP_PORT en $(ENV_FILE)"; \
		exit 1; \
	fi

	@if ! grep -q "^OPENAI_API_KEY=" $(ENV_FILE); then \
		echo "❌ Falta OPENAI_API_KEY en $(ENV_FILE)"; \
		exit 1; \
	fi

	@echo "✅ Variables de entorno requeridas encontradas:"
	@grep "^APP_PORT=" $(ENV_FILE)
	@grep "^OPENAI_API_KEY=" $(ENV_FILE) | sed 's/=.*/=********/'

build:
	$(DOCKER_COMPOSE) build

up: check-env
	$(DOCKER_COMPOSE) up

down:
	$(DOCKER_COMPOSE) down

restart: check-env
	$(DOCKER_COMPOSE) down && $(DOCKER_COMPOSE) up

logs:
	$(DOCKER_COMPOSE) logs -f

sh:
	$(DOCKER_COMPOSE) exec web /bin/sh

ps:
	$(DOCKER_COMPOSE) ps

port:
	@echo "Puerto APP_PORT=$(shell grep APP_PORT $(ENV_FILE) | cut -d '=' -f2)"

test-env:
	@echo "Variables definidas en $(ENV_FILE):"
	@cat $(ENV_FILE) | grep -v '^#' | sed 's/=.*/=********/' || echo "Archivo .env vacío"

clean:
	$(DOCKER_COMPOSE) down -v

help:
	@echo ""
	@echo "📦 Comandos disponibles para Pokedex FastAPI:"
	@echo ""
	@echo "  make build      - Construye los contenedores Docker"
	@echo "  make check-env  - Verifica que APP_PORT y OPENAI_API_KEY existan en .env"
	@echo "  make clean      - Detiene y borra volúmenes (útil para resetear todo)"
	@echo "  make down       - Detiene los contenedores"
	@echo "  make help       - Muestra esta ayuda"
	@echo "  make init       - Copia .env.example a .env si no existe"
	@echo "  make logs       - Muestra logs en tiempo real"
	@echo "  make port       - Muestra el puerto configurado"
	@echo "  make ps         - Muestra el estado de los contenedores"
	@echo "  make restart    - Reinicia los contenedores"
	@echo "  make sh         - Abre una shell en el contenedor 'web'"
	@echo "  make test-env   - Muestra las variables cargadas (oculta valores)"
	@echo "  make up         - Inicia los contenedores (requiere .env configurado)"
