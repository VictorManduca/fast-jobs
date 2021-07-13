<h1 align="center">Fast Jobs</h1>
<p align="center">A repository to learn how to do a RESTful API with Unit Test, JWT, Swagger, Python and FastAPI</p>


## Prerequisites
- python-dev or python3-dev
- python3-venv
- make
- libpq-dev
- postgres
- pgadmin

## Step-by-step
1) Install the prerequisites
2) Run `cat .env.example > .env` -> create .env file
3) Run `make create_env` -> create environment
4) Run `. ./env/bin/activate` -> activate environment
5) Run `make install_packages` -> install project's python packages
6) Run `make run_server` -> run server in the port 8000

If you want to run tests, then: `make run_test`

## URLs
- POST `/login`
- POST `/user` (create a user)

- POST `/job` (create a job)
- PATCH `/job/{id}` (update a job)
- DELETE `/job/{id}`
- GET `/job` (retrieve details of a job)
- GET `/job` (retrieve all jobs)
- GET `/job/all/active` (retrive all active jobs)

## Tests coverage
<img align="center" src="https://github.com/VictorManduca/fast-jobs/blob/main/assets/images/coverage_report.png">
