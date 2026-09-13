.PHONY: run test lint help

help:
	@echo "Доступные команды:"
	@echo "  make run   - Запустить генератор цитат"
	@echo "  make test  - Запустить модульные тесты"
	@echo "  make lint  - Проверить синтаксис файлов"

run:
	python quotes.py

test:
	python -m unittest test_quotes.py

lint:
	python -m py_compile quotes.py test_quotes.py
	@echo "Синтаксических ошибок не обнаружено."