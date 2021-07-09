.PHONY: run_server

install_packages:
	pip install -r requiriments.txt

delete_packages:
	rm -rf env/
	find . -name '__pycache__' -exec rm -rf {} +

create_env:
	python3 -m venv env

run_server:
	uvicorn src.main:app --reload