from app import app
from flask import render_template, request, jsonify



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/send-coordinates", methods=["POST"])
def send_coordinates():
    coordinates = request.json.get("coordinates")
    print("Seçilen Koordinatlar:", coordinates)
    return jsonify({"status": "success", "message": "Koordinatlar alındı"})


