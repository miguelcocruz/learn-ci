up:
	docker compose up -d --build

down:
	docker compose down

pytest:
	docker exec runtime pytest /app

ci: pytest