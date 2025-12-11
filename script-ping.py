import subprocess

hosts = ["8.8.8.8", "4.2.2.2"]

for ip in hosts:
   print(f"Testando host {ip}...")
   subprocess.run(["ping", ip])