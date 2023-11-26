from flask import Flask, jsonify, request
import pickle
from datetime import date
import os


VERSION = 1.0
MODEL_DATE = date(2023, 11, 21)

app = Flask(__name__)


file_path = "/app/rules/basic_rules.pkl"
# app.model = pickle.load(open(file_path, "rb"))


@app.route("/", methods=["GET"])
def hello_screen():
    return jsonify("Hi! Please go to /api/recommend to get a playlist recommendation!"), 200


@app.route("/api/recommend", methods=["POST"])
def get_recommendation():
    client_songs_list = request.get_json()['songs']
    recommendation = [
        rule[1] for rule in app.model if (rule[0] in client_songs_list and rule[2] >= 0.6)
    ]
    
    if len(recommendation) < 5:
        recommendation = [rule[1] for rule in app.model if (rule[0] in client_songs_list and rule[2] >= 0.4)]
        
    # Remove duplicates in recommendation
    list(set(recommendation))
    
    return jsonify(
        {
            "playlist_ids":recommendation, 
            "version": VERSION,
            "model_date": MODEL_DATE
        } 
    )


if __name__ == "__main__":
    app.run(debug=True, port=32211, host="0.0.0.0")