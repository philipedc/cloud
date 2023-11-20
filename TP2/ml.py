#--------------------------------------------------\/-----------------------------------------------------------
                                                #ML CONTAINER
from fpgrowth_py import fpgrowth

itemSetList = [['eggs', 'bacon', 'soup'],
                ['eggs', 'bacon', 'apple'],
                ['soup', 'bacon', 'banana']]
freqItemSet, rules = fpgrowth(itemSetList, minSupRatio=0.5, minConf=0.5)

freqItemSetSerializable = [list(food) for food in [group for group in freqItemSet]]

# ------------------------------------------------ \/ ------------------------------------------------------------
                                                 #WEB APP CONTAINER

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_rules():
    return jsonify(freqItemSetSerializable), 200

if __name__ == "__main__":
    app.run(debug=True, port=32211)
