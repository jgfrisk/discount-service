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


Service should now be listening to `http://localhost:5000`. Test with API documentation [link](http://localhost:5000/apidocs). <br>
(Note that this guide assumes that your Docker installation exposes services on `localhost`)

See [Makefile](./Makefile) for more commands and their details.

### Exploring the API

You can test to create discounts for a brand with default values filled in at: [http://localhost:5000/apidocs/#/discount/post_v1_discount_create](http://localhost:5000/apidocs/#/discount/post_v1_discount_create)

After codes have been created you can reserve and fetch them using this page: [http://localhost:5000/apidocs/#/discount/get_v1_discount_fetch__brand___user_](http://localhost:5000/apidocs/#/discount/get_v1_discount_fetch__brand___user_)


#### Validation examples
To demo the input value validation for the create endpoint you can try to create discounts with a missing brand/number key or try to create more than 1000 codes (configured maximum in the schema).


### Tests
If you have Python installed the API tests can be run with ```$ make run-tests```. Note that the test suite assumes that the database is empty at start so restarting the service between runs is a good idea.
