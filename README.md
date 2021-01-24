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
- Make
- Python and Requests (optional, for running API tests)
- Pip-tools (optional, for updating requirements.txt)

### Usage

Build and start the service with:
```sh
$ make build start
```

Service should now be listening to `http://localhost:5000`. Test with API documentation [link](http://localhost:5000/apidocs).

See [Makefile](./Makefile) for more commands and their details.


### Tests
If you have Python installed the API tests can be run with ```$ make run-tests```. Note that the test suite assumes that the database is empty at start so restarting the service between runs is a good idea.
