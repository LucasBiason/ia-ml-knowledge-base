.PHONY: help build up down logs clean test deploy

help: ## Mostra esta ajuda
	@echo "Financial Analysis Agent - Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

build: ## Constrói os containers
	docker-compose build

up: ## Sobe os serviços
	docker-compose up -d

down: ## Para os serviços
	docker-compose down

logs: ## Mostra os logs dos serviços
	docker-compose logs -f

clean: ## Remove containers e volumes
	docker-compose down -v --remove-orphans
	docker system prune -f

test: ## Executa os testes
	cd api && python -m pytest tests/ -v

deploy: ## Deploy completo (build + up)
	chmod +x deploy.sh
	./deploy.sh

api-logs: ## Logs apenas da API
	docker-compose logs -f financial-agent-api

web-logs: ## Logs apenas da Web
	docker-compose logs -f financial-agent-web

restart: ## Reinicia os serviços
	docker-compose restart

status: ## Status dos serviços
	docker-compose ps
