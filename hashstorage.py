import hashlib
import binascii
import json
import atexit
import os
import base64

from flask import Flask, request, jsonify, make_response
app = Flask(__name__)

def sha256(keyword): 
    bytekey = binascii.hexlify(keyword.encode("utf-8"))
    hashvalue = hashlib.sha256(bytekey).digest()
    return hashvalue.hex()

def store(data):
    key = sha256(data)
    storage[key] = data
    return key

def get(key):
    if key not in storage:
        return ""
    else:
        return storage[key]

def savejson():
    f = open("storage.json", "w")
    json.dump(storage, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

def storefile(filepath):
    with open(filepath, "r") as file:
          data = file.read()
    store(data)

@app.route("/store", methods=['POST'])
def GetStoreReq():
    params = request.json
    data = base64.b64decode(params["file"]).decode("utf-8")
    key = store(data)

    resbody = {"result": key}
    return make_response(jsonify(resbody))

@app.route("/get", methods=['POST'])
def GetGetReq():
    params = request.json
    data = get(params["key"])
    resbody = {
        'file': base64.b64encode(data.encode()).decode()
        }
    return make_response(jsonify(resbody))

if __name__ == '__main__' :
    global storage 
    if os.path.exists("./storage.json"):
        f = open('storage.json', 'r')
        storage = json.load(f)
    else:
        storage = dict()
    atexit.register(savejson)
    
    app.run(host="localhost", port=6666)
