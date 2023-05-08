.ONESHELL: all

install:
	@poetry install --no-root

compose:
	@docker-compose up -d

run-local:
	@docker-compose up -d db
	@cp compose.env .env
	@poetry run alembic upgrade head
	@poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

migrate:
	@poetry run alembic upgrade head
