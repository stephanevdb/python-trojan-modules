import socket
import requests
print("Hello from test.py")
print("This is a test module")
print(socket.gethostname())
print(requests.get("https://api.ipify.org").text)
