build:
	docker compose -f docker-compose.dev.yml build 
up:
	docker compose -f docker-compose.dev.yml up -d
start:
	docker compose -f docker-compose.dev.yml start
stop:
	docker compose -f docker-compose.dev.yml stop
down:
	docker compose -f docker-compose.dev.yml down
restart:
	docker compose -f docker-compose.dev.yml restart
logs:
	docker compose -f docker-compose.dev.yml logs -f
ps:
	docker compose -f docker-compose.dev.yml ps
shell:
	docker compose -f docker-compose.dev.yml exec fibonacci-server bash
test:
	docker compose -f docker-compose.dev.yml exec fibonacci-server pytest
deploy:
	cd fibonacci-server
	gcloud run deploy