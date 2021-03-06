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

        code = 405
        description2 = 'Invalid Request Type'


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


@app.errorhandler(405)
def explain2(e):
    return "Invalid Request: For POST Methods use JSON (Refer to Documentation For Usage)"


@app.route('/postdata', methods=['POST'])
def post_data():
    if request.method == 'POST':
        if not request.json or not 'device_uuid' in request.json:
            abort(405)

        table = dynamodb.Table('sensorMain')

        device_uuid = int(request.json['device_uuid'])

        sensor_type = (request.json['sensor_type'])
        sensor_types = ["humidity", "temperature"]
        if sensor_type not in sensor_types:
            return abort(400)

        sensor_value = (request.json['sensor_value'])
        if float(sensor_value) < 0.0 or float(sensor_value) > 100.0:
            return abort(400)

        sensor_reading_time = int(request.json['sensor_reading_time'])

        response = table.put_item(
            Item={

                'device_uuid': device_uuid,
                'sensor_type': sensor_type,
                'sensor_value': sensor_value,
                'sensor_reading_time': sensor_reading_time
            }
        )

        return jsonify(response)

    else:

        abort(405)


@app.route('/getdata/<device_uuid>/<start_time>/<end_time>', methods=['GET'])
def get_data(device_uuid, start_time, end_time):
    if request.method == "GET":

        device_uuid = int(device_uuid)
        start_time = int(start_time)
        end_time = int(end_time)
        table = dynamodb.Table('sensorMain')

        response = table.query(
            KeyConditionExpression=Key('device_uuid').eq(device_uuid)
                                   & Key('sensor_reading_time').between(start_time, end_time)
        )

        return jsonify(response)

    else:
        abort(405)


if __name__ == '__main__':
    app.debug = False
    app.run(port=8000, threaded=True)

"""
Test Runs Provided:

1. Return All device data from uuid 1 from 1501868891 until 1591409691

device_uuid = 1
start_time = 1501868891
end_time = 1591409691

http://ec2-54-237-164-186.compute-1.amazonaws.com:8000/getdata/1/1501868891/1591409691


2. Return All device data from uuid 43 from 1501868891 until 1591409691

device_uuid = 43
start_time = 1501868891
end_time = 1591409691

http://ec2-54-237-164-186.compute-1.amazonaws.com:8000/getdata/43/1501868891/1591409691


3. Insert New Data for uuid 

device_uuid = 4
sensor_type = humidity
sensor_value = 100
sensor_reading_time = 1593292

curl -i -H "Content-Type: application/json" -X POST -d '{"device_uuid": 14, "sensor_type": "humidity", "sensor_value": 99, "sensor_reading_time": 1500052521}' http://ec2-54-237-164-186.compute-1.amazonaws.com:8000/postdata
"""
