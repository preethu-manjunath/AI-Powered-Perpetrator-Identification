from flask import Flask, request, jsonify
from detect import detect_vehicles
from recognize_plate import recognize_license_plate

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['file']
    image_path = "static/uploaded.jpg"
    file.save(image_path)

    detected_vehicles_path = detect_vehicles(image_path)
    license_plate = recognize_license_plate(image_path)

    return jsonify({
        "message": "Detection Completed",
        "detected_vehicles_path": detected_vehicles_path,
        "license_plate": license_plate.strip()
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)