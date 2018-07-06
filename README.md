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
Browser (Reccomended):
Terminal: curl 
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


### Author

```python
__author__ = Sid Sachdev
__email__ = sid __dot__ sachdev9 at gmail.com
```
