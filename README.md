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

Commands will return a JSON value

```bash
Browser (Reccomended):
Terminal: curl 
```








### Author

```python
__author__ = Sid Sachdev
__email__ = sid __dot__ sachdev9 at gmail.com
```
