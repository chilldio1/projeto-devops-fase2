# Fase 2 — Projeto Docker

Aplicação web em Python com banco de dados PostgreSQL, containerizada com Docker e orquestrada com Docker Compose.

## O que o projeto faz

Conta e persiste o número de visitas recebidas. Cada requisição HTTP incrementa um contador armazenado no banco de dados.

## Tecnologias

- Python 3.11 (servidor HTTP nativo)
- PostgreSQL 15
- Docker + Docker Compose
- Multi-stage build

## Estrutura

    environment:
      POSTGRES_USER: diogo
      POSTGRES_PASSWORD: senha123
      POSTGRES_DB: estudos
    volumes:
      - postgres-dados:/var/lib/postgresql/data
      - ./init:/docker-entrypoint-initdb.d

volumes:
✅ App Python conectando no Postgres
✅ Contador de visitas incrementando
✅ Dados persistindo entre reinicializações (volume funcionando)
✅ Dois serviços orquestrados pelo Compose


Aplicação web em Python com banco de dados PostgreSQL, containerizada com Docker e orquestrada com Docker Compose.

## O que o projeto faz

Conta e persiste o número de visitas recebidas. Cada requisição HTTP incrementa um contador armazenado no banco de dados.

## Tecnologias

- Python 3.11 (servidor HTTP nativo)
- PostgreSQL 15
- Docker + Docker Compose
- Multi-stage build

## Estrutura
fase2-projeto/
├── app/
│   ├── Dockerfile        # multi-stage build
│   ├── requirements.txt
│   └── app.py
├── init/
│   └── 01-init.sql       # cria a tabela de visitas
├── docker-compose.yml
└── README.md
## Como rodar

**Pré-requisitos:** Docker e Docker Compose instalados.

```bash
git clone <url-do-repositorio>
cd fase2-projeto
docker compose up -d
```

Acesse: `http://localhost:8080`

## Comandos úteis

```bash
docker compose ps        # status dos serviços
docker compose logs app  # logs da aplicação
docker compose logs banco # logs do banco
docker compose down      # derrubar os containers
docker compose down -v   # derrubar e apagar os dados
```

## Conceitos praticados

- Dockerfile com multi-stage build
- Volumes para persistência de dados
- Redes Docker para comunicação entre containers
- Variáveis de ambiente para configuração
- Inicialização automática do banco via script SQL
