import requests as requests
import socket
from uuid import getnode as get_mac
import platform
import psutil


class PcInfo:
    hostname = ""
    public_ip = ""
    private_ip = ""
    mac_address = ""
    os = ""
    cpu = ""
    ram = ""
    storage = ""


pcinfo = PcInfo()

pcinfo.public_ip = requests.get('https://api.ipify.org').text
pcinfo.hostname = socket.gethostname()
pcinfo.mac_address = get_mac()
pcinfo.os = platform.platform()
pcinfo.cpu = platform.processor()
pcinfo.ram = psutil.virtual_memory().total
pcinfo.storage = psutil.disk_usage('/')

if __name__ == '__main__':
    print("Public IP: " + pcinfo.public_ip)
    print("Hostname: " + pcinfo.hostname)
    print("MAC Address: " + pcinfo.mac_address.__str__())
    print("OS: " + pcinfo.os)
    print("CPU: " + pcinfo.cpu)
    print("RAM: " + pcinfo.ram.__str__())
    print("Free GiB: " + (pcinfo.storage.free / (2 ** 30)).__round__(2).__str__())
