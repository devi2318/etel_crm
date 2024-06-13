# Local setup

1. Clone the repo and `cd` into it:

```
git clone https://github.com/cloudetel/etel_crm.git && cd etel_crm
```

2. Copy the env.example files to .env files and fill in the values:

```
cp .env.example .env && cp frontend/.env.example frontend/.env
```

3. Setup pre-commit hook:

```
pre-commit install
```

> Note you may need to install pre-commit if not already installed.

4. Setup docker:

```
docker-compose up -d && docker-compose exec backend alembic upgrade head
```

5. Testing:

> Note that the docker containers are up and running, otherwise run the second command.
```
docker compose exec -T backend bash /app/tests-start.sh "$@"
```

```
/scripts/test.sh
```
