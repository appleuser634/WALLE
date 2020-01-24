import subprocess
import time

print("Hi")

i = 0
while True:
    
    if i == 30: 
        print("DID YOU UPDATE?")

        cmd = "git pull"
        subprocess.call(cmd, shell=True)

    print(i)
    i += 1

    time.sleep(1)
