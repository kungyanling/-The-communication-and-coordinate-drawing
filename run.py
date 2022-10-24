import os
import subprocess
import json
import time

s = os.system("make")
assert s == 0
time.sleep(1)
p_c = subprocess.Popen(["./client"])
p_s = subprocess.Popen(["python3","sever.py"])
while p_s.poll() == None:
	continue
p_c.kill()
p_s.kill()
