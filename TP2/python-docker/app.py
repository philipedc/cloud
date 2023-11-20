from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_rules():
    return jsonify("Hello World"), 200


if __name__ == "__main__":
    app.run(debug=True, port=32211, host="0.0.0.0")