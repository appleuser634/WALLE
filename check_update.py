import subprocess

print("Did you Update?")

cmd = "git pull"
subprocess.call(cmd, shell=True)
