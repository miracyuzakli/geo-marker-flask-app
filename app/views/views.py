from app import app
from flask import render_template, request, jsonify



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/send-coordinates", methods=["POST"])
def send_coordinates():


    data = request.json
    city = data.get('city')
    sale_date = data.get('sale_date')
    property_type = data.get('property_type')
    price_amount = data.get('price_amount')
    lot_size = data.get('lot_size')
    coordinates = data.get('coordinates')


    return jsonify({"status": "success", "message": "Koordinatlar alındı"})


