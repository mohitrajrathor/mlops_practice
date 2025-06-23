.PHONY: venv install lint test run

venv:
	python3 -m venv .venv

install: venv
	. .venv/bin/activate && python -m pip install -r requirements.txt

lint:
	. .venv/bin/activate && flake8 main.py

test:
	. .venv/bin/activate && pytest test_main.py

run:
	. .venv/bin/activate && python main.py
