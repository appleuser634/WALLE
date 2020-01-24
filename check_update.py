import subprocess

print("DID YOU UPDATE?")
print("Hello!")

cmd = "git pull"
subprocess.call(cmd, shell=True)
