import os
from generator import generator
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def rootRoute():
    return jsonify({
        "message": 'Sup bitch'
})

@app.route('/generate', methods=['POST'])
def generateDate():
    data = request.get_json()
    try:
        rows = data["rows"]
        format = data["format"]
        schema = data["schema"]
    except:
        return jsonify({
            "message": "Key required"
        })
    schema = eval(schema)
    generated = generator(schema=schema, rows=5)
    return jsonify({
        "you sent": data,
        "generated": generated
    })
    

if __name__ == '__main__':
    app.run(debug=True,port=os.getenv("port", default=5500))