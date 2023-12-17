.PHONY: run-local
run-local:
	poetry run uvicorn --host=localhost --port=8000 Backyard.main:app --reload --lifespan=on
