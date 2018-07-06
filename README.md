# Canary Security Device
Canary Security Data Center 

### Tools Used:

- Flask (Python) (Required)
- AWS EC2 (Project is Live for testing)
- [AWS DynamoDB](https://https://aws.amazon.com/dynamodb/ "AWS DynamoDB") (Fast & Flexible DB Service (Recommended for IoT Devices))
- Gunicorn (Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX (Allows to run it asynchronously))
- Gevent (To add workers (Used with Gunicorn))

## Data Model

```
5000 User Data Auto Generated (Hence different device_id)

device_uuid (0 .. 50)
sensor_type ("humidity", "temperature")
sensor_value (0.0 .. 100.0)
sensor_reading_time (Used Epoch Converter - Dates From 4th July 2017 until 4th July 2018)
```

## Usage

As the project is live, you aren't required to install/worry about dependencies
###### A requirements.txt has still been provided to run locally (Just replace the ec2 IP with localhost:8000/
Commands will return a JSON value

```bash
Browser (Reccomended): http://ec2-54-237-164-186.compute-1.amazonaws.com:8000/getdata/1/1501868891/1591409691
Terminal: curl ec2-54-237-164-186.compute-1.amazonaws.com:8000/getdata/43/1501868891/1591409691
```

## Design Decisions

- Flask: 
  - The project didn't require any API authentication and authorization, so didn't require Django. 
  - Flask is generally faster in performance compared to Django as it is much minimal in design
  - Didn't need the ORM used in Django
  - Django relies heavily on it's relational database integration. Flask allowed the ease of use with NoSQL  

- AWS DynamoDB:
  - DynamoDB NoSQL allows great flexibility and is recommended for IoT devices for the constant stream of data 
  - With the auto scaling based on usability and the ability to set the priority of reads or writes, it was a great option
  - The "scan" on the db is set to the sensor_reading_time to provide maximum speed
  - insertData.py is provided for an easy json upload to the db


## Tests 

```
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

http://ec2-54-237-164-186.compute-1.amazonaws.com:8000/postdata?device_uuid=4&sensor_type=humidity&sensor_value=100&sensor_reading_time=1593292

```

### Author

```python
__author__ = Sid Sachdev
__email__ = sid __dot__ sachdev9 at gmail.com
```
