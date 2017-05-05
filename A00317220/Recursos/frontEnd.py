from flask import Flask, abort, request
from flask_restplus import Resource, Api
from flask_restplus import  fields
import json

from logica import memoria, get_espacioDisco, get_cpu, getEstado

app = Flask(__name__)
#api_url= '/v1.0'

api = Api(app,version='1', title='API EN SWAGGER', description="recursos cpu")
ns = api.namespace('v1/information',description='recursos')
@ns.route('/')
#@app.route(api_url+'/information', methods=['GET'])
class informacion(Resource):
 @api.response(200,'recursos consumidos')
 def get(self):
  list = {}

  list["RAM en uso"] = memoria()[0]
  list["Espacio de disco disponible"]= get_espacioDisco()[1]	
  list["Consumo de CPU"]= get_cpu()[2]
  list["Estado del servicio sshd"]= getEstado()[0]
  return json.dumps(list),200

 @api.response(404,'HTTP 404 NOT FOUND')
 def post(self):
  return "HTTP 404 NOT FOUND",404


 @api.response(404,'HTTP 404 NOT FOUND')
 def put(self):
  return "HTTP 404 NOT FOUND",404


 @api.response(404,'HTTP 404 NOT FOUND')
 def delete(self):
  return "HTTP 404 NOT FOUND",404


if __name__=="__main__":

  app.run(host='0.0.0.0', port=8080, debug='True')
