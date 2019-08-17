#!/bin/python

//please change INFLUXDBIP,DATABASENAME,IPADRESSBLYNK,ENTERATUHTOKEN

from urllib2 import Request, urlopen
from influxdb import InfluxDBClient
client = InfluxDBClient(host='INFLUXDBIP', database='DATABASENAME')
while True:
    Pin = 0
    while Pin <  24:
        try:
        
            P = str(Pin)
            request = Request('http://IPADRESSBLYNK:8080/ENTERAUTHTOKEN/get/V%s' % P)
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
 





  






