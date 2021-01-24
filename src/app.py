from flask import Flask, jsonify, request

from discounts import create_discount_codes
from models import Discount, db


app = Flask(__name__)

# Configure a local SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/local_file_database.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # suppress warning

# Initialize database engine, create tables and setup application context
db.init_app(app)
app.app_context().push()
db.create_all()


@app.route("/test")
def test():
    """ Helper endpoint to check if service is up and responding """
    return jsonify({"status": "OK"}), 200


@app.route("/v1/create", methods=["POST"])
def create_discounts():
    """
    Generate a number of discount codes for a brand, insert them
    into a database and return a list with the codes.
    """

    brand = request.json["brand"]
    number_to_create = request.json["number_to_create"]

    discount_codes = create_discount_codes(number_to_create)

    # Insert into database
    # Note that this could fail in the event of a (very unlikely) collission
    # but in this case we can just retry the operation after generating a new
    # list of codes or just let the client retry the call
    for discount_code in discount_codes:
        db.session.add(Discount(code=discount_code,brand=brand))
    db.session.commit()


    return jsonify(discount_codes)
