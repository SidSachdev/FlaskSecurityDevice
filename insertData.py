from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('sensorMain')

with open("GeneratedUserDeviceData.json") as json_file:
    sensorData = json.load(json_file, parse_float=decimal.Decimal)
    for data in sensorData:
        ide = data['device_uuid']
        sensor_type = data['sensor_type']
        sensor_value = int(data['sensor_value'])
        sensor_reading_time = int(data['sensor_reading_time'])

        print("Adding Device Data: ", ide)

        table.put_item(
           Item={
               'device_uuid': ide,
               'sensor_type': sensor_type,
               'sensor_value': sensor_value,
               'sensor_reading_time': sensor_reading_time
            }
        )
