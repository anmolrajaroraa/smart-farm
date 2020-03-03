from flask import Flask,request,jsonify
from flask_cors import CORS,cross_origin
import random
import json

app=Flask(__name__)
CORS(app, support_credentials=True)

num_1 = random.randint(1,10)

@app.route('/api/test', methods=['POST', 'GET','OPTIONS'])
@cross_origin(supports_credentials=True)
def index():
    import test2_json
    num_2 = random.randint(1,10)
    with open('data.json') as f:
        data = json.load(f)
    return jsonify({"data" : data})
    # if num_2 == num_1:
    #     return jsonify({"status":"Data Changed", "num_1":num_1,"num_2":num_2})
    # else:
    #     return jsonify({"status":"Not Changed","num_1":num_1,"num_2":num_2})

if __name__=="__main__":
    app.run(host='127.0.0.1', port=8000)