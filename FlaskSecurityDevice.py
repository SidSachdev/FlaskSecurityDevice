from __future__ import print_function  # Python 2/3 compatibility
from flask import Flask, request, jsonify
import boto3
import json
import werkzeug.exceptions as ex
import decimal
from boto3.dynamodb.conditions import Key


class InvalidData(ex.HTTPException):
    def __init__(self):
        code = 400
        description = 'Data provided is Invalid or Insufficient'


ex.default_exceptions[400] = InvalidData
abort = ex.Aborter()

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)

            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


app.json_encoder = DecimalEncoder


@app.route('/')
def hello_world():
    return 'Welcome: Canary Device Data Center'

@app.errorhandler(400)
def explain(e):
    return "Data provided is Invalid or Insufficient"


@app.route('/postdata', methods=['GET', 'POST', 'PUT'])
def post_data():
    device_id = int(request.args.get("device_id"))

    sensor_type = request.args.get("sensor_type")
    sensor_types = ["humidity", "temperature"]
    if sensor_type not in sensor_types:
        return abort(400)

    sensor_value = request.args.get("sensor_value")
    if float(sensor_value) < 0.0 or float(sensor_value) > 100.0:
        return abort(400)

    sensor_reading_time = int(request.args.get("sensor_reading_time"))
    # example.com?arg1=value1&arg2=value2

    table = dynamodb.Table('sensorMain')
    response = table.put_item(
        Item={
            'device_id': device_id,
            'sensor_type': sensor_type,
            'sensor_value': sensor_value,
            'sensor_reading_time': sensor_reading_time
        }
    )

    return jsonify(response)