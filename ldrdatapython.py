
import Adafruit_IO as afio
import requests
url='https://api.thingspeak.com/update?api_key=Y2ZUEG48XPCSN3PT&field1={}'
from serial import Serial
s=Serial('COM5',9600)

uname='gaurav_123'
akey='aio_oYoI95oMldkCkAiLBrQzMTUB0Gft'
aio=afio.Client(uname,akey)
feed=aio.feeds('ga')
while True:
  if s.in_waiting:
      r=s.readline().decode().strip('\r\n')
       r=aio.receive(feed.key)
   print(r.value)
   v=requests.get(url.format(r))
   data=r.value+'\r\n'
   s.write(data.encode())

  
