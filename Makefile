.PHONY: help setup test lint check environment clean

help:
	@echo "Modern Time Series Lab"
	@echo ""
	@echo "make setup        Install the locked project environment"
	@echo "make test         Run automated tests"
	@echo "make lint         Run Ruff"
	@echo "make check        Run lint and tests"
	@echo "make environment  Print reproducibility/environment information"
	@echo "make clean        Remove local Python/test caches"

setup:
	uv sync --locked

test:
	uv run pytest

lint:
	uv run ruff check .

check: lint test

environment:
	uv run python scripts/check_environment.py

clean:
	rm -rf .pytest_cache .ruff_cache .mypy_cache htmlcov
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
