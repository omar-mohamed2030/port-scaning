#!/bin/python3
import sys
import socket
from datetime import datetime
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Invalid choice. Usage: python3 scanner.py <ip>")
    sys.exit() 
print("*" * 50)
print("Scanning Target: " + target)
print("Time started: " + str(datetime.now()))
print("*" * 50)

try:
    for port in range(50, 81):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) 
        result = soc.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port} is open")
        
        soc.close() 

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()
