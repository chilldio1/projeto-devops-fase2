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
  postgres-dados:
EOF
Depois recria os containers:
bashdocker compose down
docker compose up -d
docker ps
Me cola o resultado do docker ps — agora deve aparecer a porta 8080 mapeada no container app.agora esta ok, rodei o curl e apareceu a minha visitaExcelente! Agora testa mais duas vezes:
bashcurl http://localhost:8080
curl http://localhost:8080
O contador deve incrementar a cada chamada — isso prova que a app está conectando no Postgres e persistindo os dados corretamente.
Depois derruba tudo sem -v e sobe de novo:
bashdocker compose down
docker compose up -d
Aguarda uns 5 segundos e testa:
bashcurl http://localhost:8080
O número de visitas deve continuar de onde parou — isso prova que o volume está funcionando e os dados persistiram mesmo com os containers recriados.
Me cola os resultados!isso mesmo, continuou de onde pareiPerfeito! O projeto está funcionando completamente:

✅ App Python conectando no Postgres
✅ Contador de visitas incrementando
✅ Dados persistindo entre reinicializações (volume funcionando)
✅ Dois serviços orquestrados pelo Compose


Agora falta só o README — é o que transforma esse projeto num item de portfólio real. Recrutadores e tech leads olham o README antes de qualquer coisa.
bashnano ~/projeto-devops/fase2-projeto/README.md
Cole isso (personalize à vontade):
markdown# Fase 2 — Projeto Docker

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
