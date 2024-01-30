from app import app
from flask import render_template, request, jsonify
from services import get_request_data,scrape_function

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


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

