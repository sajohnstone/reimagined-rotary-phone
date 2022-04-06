SHELL := /bin/bash
init:
	python3 -m venv ./.venv
	source ./.venv/bin/activate
	pip3 install -r requirements.txt
	pip3 install -r requirements-dev.txt

run:
	python3 -m app.main

lint:
	safety check -r requirements.txt
	bandit -r app
	isort app tests
	black app tests
	flake8 app tests

unittest:
	pytest tests/unit --cov=app --cov-fail-under=100 || coverage report -m

clean:
	rm -rf ./.venv