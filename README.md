## Prerequisites

- python-dev or python3-dev
- python3-venv
- make
- libpq-dev
- postgres
- pgadmin

## Step-by-step
1) Install the prerequisites
2) Run `make create_env` -> craete environment
3) Run `. ./env/bin/activate` -> activate environment
4) Run `make install_packages` -> install project's python packages
5) Run `make run_server` -> run server in the port 8000

If you want to run tests, then: `make run_test`
