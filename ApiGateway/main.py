from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve
import datetime
import requests
import re
import json

app = Flask(__name__)
cors = CORS(app)

#  TEST DE SERVICIO # 

@app.route("/", methods=['GET'])
def test():
    #variable de paso
    Json = {}
    Json["Message"] = "Server Running ..."
    return jsonify(Json)


# CONEXION # ESTA FUNCION CARGA ARCHIVO DE CONFIGURACIONES #

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    dataConfig = loadFileConfig()
    print("Server url-backend running : http://"+ 
        dataConfig["url-backend"]+ ":"+
        dataConfig["port"])
    serve(app, host=dataConfig["url-backend"], 
        port=dataConfig["port"])    

