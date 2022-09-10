import os
from generator import generator
from flask import Flask, jsonify, request
from flask_cors import CORS
from generators import generators

app = Flask(__name__)
CORS(app)


@app.route('/')
def rootRoute():
    return jsonify({
        "message": 'Sup bitch'
}), 200

@app.route('/generators')
def getGenerators():
    gens = []
    for generator in generators:
        gens.append(generator['alias'])
    return jsonify({
        "generators": gens
    }), 200

@app.route('/generate', methods=['POST'])
def generateDate():
    data = request.get_json()
    try:
        rows = data["rows"]
        # format = data["format"]
        schema = data["schema"]
    except:
        return jsonify({
            "message": "Key required"
        }), 400
    try:
        generated = generator(schema=schema, rows=rows)
    except:
         return jsonify({
            "message": "Something went wrong"
         }), 500
    return jsonify({
        "generated": generated
    }), 200
    

if __name__ == '__main__':
    app.run(debug=True,port=os.getenv("port", default=5500))