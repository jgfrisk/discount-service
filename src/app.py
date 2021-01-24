from flask import Flask, jsonify, request
from discounts import create_discount_codes

app = Flask(__name__)


@app.route("/test")
def test():
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

    return jsonify(discount_codes)
