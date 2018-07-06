from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


table = dynamodb.create_table(
    TableName='sensorMain',
    KeySchema=[
        {
            'AttributeName': 'device_uuid',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'sensor_reading_time',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'device_uuid',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'sensor_reading_time',
            'AttributeType': 'N'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)