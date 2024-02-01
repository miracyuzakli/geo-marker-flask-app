from app import app
from flask import render_template, request, jsonify
from services import get_request_data,scrape_function
import json


@app.route("/")
@app.route("/index")
def index():

    with open('data/cities.json', 'r', encoding='utf-8') as file:
        cities_data = json.load(file)


    # print(cities_data)

    return render_template("index.html", cities= cities_data)


@app.route("/send-coordinates", methods=["POST"])
def send_coordinates():
    data = request.json
    city = data.get("city")
    sale_date = data.get("sale_date")
    property_type = data.get("property_type")
    price_amount = data.get("price_amount")
    lot_size = data.get("lot_size")
    coordinates = data.get("coordinates")

    get_request_data(
        city=city,
        sale_date=sale_date,
        property_type=property_type,
        price_amount=price_amount,
        lot_size=lot_size,
        coordinates=coordinates
    )



    return jsonify({"status": "success"})

