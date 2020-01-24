import subprocess

print("DID YOU UPDATE?")

cmd = "git pull"
subprocess.call(cmd, shell=True)
