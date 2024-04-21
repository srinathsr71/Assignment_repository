from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/submit-json', methods=['POST'])
def submit_json():
    if request.is_json:
        # Extract JSON data from the request
        data = request.json
        if 'name' in data and 'email' in data:
            name = data['name']
            email = data['email']
            return jsonify({"message": f"Received data: Name - {name}, Email - {email}"}), 200
        else:
            return jsonify({"error": "Name and email fields are required."}), 400
    else:
        return jsonify({"error": "Invalid JSON payload."}), 400
if __name__ == '__main__':
    app.run(debug=True)
