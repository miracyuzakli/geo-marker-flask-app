from app import app
from flask import render_template, request, jsonify
from services import GeoWarehouseScraper
import json

scrabe = GeoWarehouseScraper()

city = {
    "Algoma": "01",
    "Brant": "02",
    "Bruce": "03",
    "Cochrane": "06",
    "Dufferin": "07",
    "Dundas": "08",
    "Durham": "40",
    "Elgin": "11",
    "Essex": "12",
    "Frontenac": "13",
    "Glengarry": "14",
    "Grenville": "15",
    "Grey": "16",
    "Haldimand": "18",
    "Haliburton": "19",
    "Halton": "20",
    "Hamilton": "62",
    "Hastings": "21",
    "Huron": "22",
    "Kenora": "23",
    "Kent": "24",
    "Lambton": "25",
    "Lanark": "27",
    "Leeds": "28",
    "Lennox": "29",
    "Manitoulin": "31",
    "Middlesex": "33",
    "Muskoka": "35",
    "Niagara North": "30",
    "Niagara South": "59",
    "Nipissing": "36",
    "Norfolk": "37",
    "Northumberland": "39",
    "Ottawa-Carleton": "04",
    "Oxford": "41",
    "Parry": "42",
    "Peel": "43",
    "Perth": "44",
    "Peterborough": "45",
    "Prescott": "46",
    "Prince": "47",
    "Rainy": "48",
    "Renfrew": "49",
    "Russell": "50",
    "Simcoe": "51",
    "Stormont": "52",
    "Sudbury": "53",
    "Thunder": "55",
    "Timiskaming": "54",
    "Toronto": "80",
    "Victoria": "57",
    "Waterloo": "58",
    "Wellington": "61",
    "York": "65",
}


@app.route("/")
@app.route("/index")
def index():

    with open("data/data1.json", "r", encoding="utf-8") as file:
        cities_data = json.load(file)

    citys = list()

    for i in city:
        citys.append(i)

    return render_template("index.html", cities=cities_data, city=citys)


@app.route("/send-coordinates", methods=["POST"])
def send_coordinates():

    data = request.json
    city = data.get("city")
    city_name = data.get("city_name")
    sale_date = data.get("sale_date")
    property_type = data.get("property_type")
    price_amount = data.get("price_amount")
    lot_size = data.get("lot_size")
    coordinates = data.get("coordinates")

    scrabe.run_scrabe(
        city=city,
        city_name=city_name,
        sale_date=sale_date,
        property_type=property_type,
        price_amount=price_amount,
        lot_size=lot_size,
        coordinates=coordinates,
    )

 

    return jsonify({"status": "success"})
