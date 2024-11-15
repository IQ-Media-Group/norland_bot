restart:
	git fetch
	git pull
	docker compose up --build -d

install:
	poetry install --no-root
	$(MAKE) restart
