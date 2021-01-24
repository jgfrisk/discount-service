# Discount Service

## Description

Basic setup for a service to generate discount codes using:
- Python 3.8
- Flask
- Gunicorn
- Flask-SQLAlchemy
- Flasgger
- SQLite

## Running the service

### Prerequisites
- Docker
- Make (optional, see below)
- Python and Requests (optional for running API tests)
- Pip-tools (optional for updating requirements.txt)

### Usage

Build and start the service with:
```sh
$ make build start
```

Service should now be listening to `http://localhost:5000` and a test endpoint at [http://localhost:5000/test](http://localhost:5000/test) See [Makefile](./Makefile) for more targets, their details and commands to run service without make.
