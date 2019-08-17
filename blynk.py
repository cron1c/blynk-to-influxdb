#!/bin/python
from urllib2 import Request, urlopen
from influxdb import InfluxDBClient
client = InfluxDBClient(host='192.168.178.74', database='blynk')
while True:
    Pin = 0
    while Pin <  24:
        try:
        
            P = str(Pin)
            p = str(Pin)
            request = Request('http://192.168.178.74:8080/abK9uJZW1fx0_CZwfu5mO1ml0B-U1DQj/get/V%s' % P)
            Pin += 1
            response_body = urlopen(request).read()
            response = response_body[2:-2]
            print response
            measurement = [
                    {
                        "measurement": "V%s" % P,
                        "tags" : {
                            "machine": "silvia"
                            },
                        "fields" : {
                            "value": response
                            }
                        }
                    ]
        
            client.write_points(measurement) 
            time.sleep(10)
        except:
            continue 
 





  






