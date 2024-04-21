from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/submit-json', methods=['POST'])
def submit_json():
    if request.is_json:
        data = request.json
        # Process JSON data
        return jsonify({"message": "Received JSON data"}), 200
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        # Process form data
        return jsonify({"message": f"Received form data: Name - {name}, Email - {email}"}), 200
if __name__ == '__main__':
    app.run(debug=True)
