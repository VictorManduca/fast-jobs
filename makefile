.PHONY: run_server

create_env:
	python3 -m venv env

delete_packages:
	rm -rf env/
	find . -name '__pycache__' -exec rm -rf {} +

install_packages:
	pip install -r requirements.txt

uninstall_packages:
	pip freeze|xargs pip uninstall -y

run_server:
	uvicorn src.main:app --reload

