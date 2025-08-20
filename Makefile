.PHONY: help install test run docker-build docker-run docker-test clean

help:
	@echo "Available commands:"
	@echo "  install      - Install Python dependencies"
	@echo "  test         - Run tests"
	@echo "  run          - Run the calculator"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-run   - Run Docker container"
	@echo "  docker-test  - Run tests in Docker container"
	@echo "  clean        - Clean up cache files"

install:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	pytest test_calculator.py -v

run:
	python calculator.py

docker-build:
	docker build -t calculator-app .

docker-run:
	docker run calculator-app

docker-test:
	docker run calculator-app python -m pytest test_calculator.py -v

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
