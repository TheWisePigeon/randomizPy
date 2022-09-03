from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def rootRoute():
    return jsonify({
        "message": 'Sup bitch'
    })

if __name__ == '__main__':
    app.run(debug=True,port=os.getenv("port", default=5500))