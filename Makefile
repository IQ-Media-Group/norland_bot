restart:
	poetry run python main.py

install:
	poetry install --no-root
	$(MAKE) restart
