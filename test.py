import os
import subprocess
subprocess.run('pip install socket')
import socket

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

print("Your IP address is:", get_ip_address())
