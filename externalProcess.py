import time
import subprocess
'''
for i in range(1000000):
    print i
    time.sleep(1)
'''


pingTime = subprocess.Popen('ping www.google.com -t', stdout=subprocess.PIPE)

while True:
    output = pingTime.stdout.readline()
    if output == '' and pingTime.poll() is not None:
        break
    if output:
        print output.strip()
