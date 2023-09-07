import socket
import subprocess
import sys
from datetime import datetime


subprocess.call('clear', shell=True)

Scan_server = input("Enter a host to scan: ")
Scan_server_ip = socket.gethostbyname(Scan_server)

print("_" * 60)
print("Scanning Host", Scan_server_ip)
print("_" * 60)

currentT =datetime.now()

try:
    for port in range(1,5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((Scan_server_ip, port))
        if result == 0:
            print("Port {}:    Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You have ended the script")
    sys.exit()

except socket.gaierror:
    print("Host couldnt be resolved")
    sys.exit()

except socket.error:
    print("Connection Failed")
    sys.exit()

exitT =datetime.now()

totalT = exitT - currentT

print("Scan completed in:")
print(totalT)
