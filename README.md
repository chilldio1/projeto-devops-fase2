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
curl: (7) Failed to connect to localhost port 8080 after 1 ms: Could not connect to serverA porta não está sendo exposta. Repara que no docker ps o container fase2-projeto-app-1 não mostra nenhuma porta mapeada — diferente do banco que mostra 5432/tcp.
Isso significa que o Compose não aplicou o ports corretamente. Vamos verificar o arquivo:
bashcd ~/projeto-devops/fase2-projeto
cat docker-compose.yml
Presta atenção na indentação do ports — em YAML, ele precisa estar no mesmo nível que build, environment e depends_on, dentro do serviço app:
yamlservices:
  app:
    build: ./app
    ports:            # ← mesmo nível que build
      - "8080:8080"
    environment:
      ...
Se a indentação estiver errada (um espaço a mais ou a menos), o YAML ignora a configuração silenciosamente. Me cola o resultado do cat docker-compose.yml.Achei o problema! A indentação está inconsistente. Repara:
yaml  app:
    build: ./app    # 4 espaços ✅
    ports:          # 4 espaços ✅
      - "8080:8080" # 6 espaços ✅
    environment:    # 4 espaços ✅
Mas olhando a imagem, build, ports, environment e depends_on estão com 4 espaços, enquanto banco: está com 2 espaços — isso é inconsistência que pode estar confundindo o parser do YAML.
Vamos reescrever o arquivo do zero pra garantir:
bashcat > docker-compose.yml << 'EOF'
services:
  app:
    build: ./app
    ports:
      - "8080:8080"
    environment:
      DB_HOST: banco
      DB_NAME: estudos
      DB_USER: diogo
      DB_PASSWORD: senha123
    depends_on:
      - banco

  banco:
    image: postgres:15
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
