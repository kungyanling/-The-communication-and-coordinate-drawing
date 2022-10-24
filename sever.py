import zmq
import time
import random
import json
import math
import folium
import os

address = "tcp://127.0.0.1:5566"
context = zmq.Context()
# 使用 zmq.REP 模式，做為 server 端
socket = context.socket(zmq.REP)
# bind(位置) - 將位置綁定到socket   //client 和 server 需綁定相同位置
socket.bind(address) 
# 等待連線
time.sleep(1)
print("Sever Working...")
while True:
    message = socket.recv()
    msg = int.from_bytes(message, "big")
    if msg == 0:
    	break
    XX = random.randint( 50, 100) 
    msgXX = msg + XX
    #bytes_val = msgXX.to_bytes(10000, 'big') False!! Every Reply is 0!
    bytes_val = msgXX.to_bytes(100000, 'little')
    socket.send(bytes_val)
time.sleep(1)
with open("./location.json","r") as f:
 	p = json.load(f)
result = []
n = math.ceil(len(p) / 2) 
idx = 0
for t in range(n):
  result.append(p[idx : idx + 2])
  idx = idx + 2
C = folium.Map(result[0], zoom_start=10)
location=result
route = folium.PolyLine(  
    location,   
    weight = 3,  
    color ='purple',  
    opacity = 1  
).add_to(C)
for tt in range(0,len(result)):
    M = folium.Marker(location = result[tt],
                   popup = 'location[%d]' % (tt+1))
    C.add_child(child=M)
C.save(os.path.join(r'/home/anny/Desktop/Anny', 'map.html'))
