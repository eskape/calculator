from flask import Flask
from flask import request
from flask_restful import Resource, Api, reqparse
from Calculator import Calculator

app = Flask(__name__)
api = Api(app)


class Add(Resource):

    def post(self):
        calculator = Calculator()

        json_data = request.get_json(force=True)
        val1 = json_data['val1']
        val2 = json_data['val2']
        result = calculator.add(int(val1), int(val2))

        return {'Result': result}

api.add_resource(Add, '/add')

if __name__ == '__main__':
     app.run(port='5002')