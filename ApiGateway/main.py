from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve
import datetime
import requests
import re
import json

app = Flask(__name__)
cors = CORS(app)

# LIBRERIAS JWT #

from flask_jwt_extended import create_access_token, verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# CREACION TOKEN #

app.config["JWT_SECRET_KEY"] = 'top-secret' #puede llevar cualquier nombre
jwt = JWTManager(app)


@app.route("/login", methods=['POST'])
def create_token():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-security"]+"/usuarios/validar"
    response = requests.post(url, json= data, headers=headers)
    if response.status_code == 200:
        user = response.json()
        expires = datetime.timedelta(seconds=60*60*24)
        access_token = create_access_token(identity=user,
            expires_delta=expires)
        return jsonify({"token": access_token,
            "user_id": user["_id"]})
    else:
        return jsonify({
            "Message": "correo o contraseña incorrecto. "
        }), 401  


# MIDDLEWARE #

def limpiarUrl(url):
    partes = request.path.split("/")
    for laParte in partes:
        if re.search('\\d', laParte): 
           url = url.replace(laParte, "?")

    return url


def validarPermiso(endPoint, metodo, idRol):
    url = dataConfig["url-backend-security"]+"/permisos-roles/validar-permiso/rol/"+str(idRol)
    tienePermiso= False
    headers= {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url": endPoint,
        "metodo": metodo
    }
    response = requests.get(url, json=body, headers=headers)
    try:
        data = response.json()
        if("_id" in data):
            tienePermiso =True
    except: 
        pass
    return tienePermiso   




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

