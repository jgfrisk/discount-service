from flask import Flask, jsonify, request, abort
from flasgger import Swagger, swag_from

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

# Init Flassger
swagger = Swagger(app)


@app.route("/test")
def test():
    """ Helper endpoint to check if service is up and responding """
    return jsonify({"status": "OK"}), 200


@app.route("/v1/create", methods=["POST"])
@swag_from("swagger/create_validation.yml", validation=True)
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


@app.route("/v1/fetch/<string:brand>/<string:user>", methods=["GET"])
@swag_from("swagger/fetch_validation.yml", validation=False)
def fetch_discount(brand: str, user: str):
    """
    Reserve and fetch a discount code for a specified brand and user
    """

    # find and reserve a code for (brand, user) OR
    # return a previously reserved code if one exists
    record = Discount.query.filter_by(user=user, brand=brand).first()

    if record != None:
        # Previously reserved code exists
        discount_code = record.code

    else:
        # Check that brand has unreserved codes
        unreserved_record = Discount.query.filter_by(brand=brand).filter(Discount.user == None).first()

        if unreserved_record != None:

            # update database
            unreserved_record.user = user
            db.session.merge(unreserved_record)
            db.session.commit()

            discount_code = unreserved_record.code

            # Brand can be notified here
            print(f"Notification for brand: {brand} and user: {user} ")

        else:
            abort(404, "No codes for brand exist")


    return jsonify({"discount_code": discount_code})
