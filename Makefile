up:
	docker compose up -d

down:
	docker compose down

pytest:
	pytest /app

ci:
	pytest