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

###### A requirements.txt has still been provided to run locally Just replace the ec2 IP with localhost:8000/
###### Will require additional authentication to access the DB (New Security Group will be added based on requirement)

Commands will return a JSON value

```bash
Browser: http://ec2-54-237-164-186.compute-1.amazonaws.com:8000/getdata/1/1501868891/1591409691
Terminal: curl ec2-54-237-164-186.compute-1.amazonaws.com:8000/getdata/43/1501868891/1591409691
Terminal(POST): curl -i -H "Content-Type: application/json" -X POST -d '{"device_uuid": 14, "sensor_type": "humidity", "sensor_value": 99, "sensor_reading_time": 1500052521}' http://ec2-54-237-164-186.compute-1.amazonaws.com:8000/postdata
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

curl -i -H "Content-Type: application/json" -X POST -d '{"device_uuid": 14, "sensor_type": "humidity", "sensor_value": 99, "sensor_reading_time": 1500052521}' http://ec2-54-237-164-186.compute-1.amazonaws.com:8000/postdata

```

## Apache Benchmark Testing Results (Concurrency level 100) (Total Requests 200)

```
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 100 requests
Completed 200 requests
Finished 200 requests


Server Software:        gunicorn/19.9.0
Server Hostname:        localhost
Server Port:            8000

Document Path:          /getdata/1/1501868891/1591409691
Document Length:        9393 bytes

Concurrency Level:      100
Time taken for tests:   4.820 seconds
Complete requests:      200
Failed requests:        0
Total transferred:      1909400 bytes
HTML transferred:       1878600 bytes
Requests per second:    41.50 [#/sec] (mean)
Time per request:       2409.754 [ms] (mean)
Time per request:       24.098 [ms] (mean, across all concurrent requests)
Transfer rate:          386.90 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   14  14.0     19      35
Processing:   533 1918 761.2   1847    3967
Waiting:      523 1912 762.9   1838    3967
Total:        533 1932 764.1   1864    4002

Percentage of the requests served within a certain time (ms)
  50%   1864
  66%   2293
  75%   2497
  80%   2641
  90%   2723
  95%   2932
  98%   3963
  99%   3988
 100%   4002 (longest request)
```

## Future Advancements

- PUT Method will allow us to update data based on parameters
- DELETE Method will allow the deletion of certain values if deemed invalid

### Author

```python
__author__ = Sid Sachdev
__email__ = sid __dot__ sachdev9 at gmail.com
```
