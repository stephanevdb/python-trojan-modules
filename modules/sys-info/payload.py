import os

import requests as requests
import socket
from uuid import getnode as get_mac
import platform
import psutil
import random
import string
import ftplib


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
    print("Gathering system information...")
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    f = open(result_str + "-output.txt", "a")
    f.write("Public IP: " + pcinfo.public_ip + "\n")
    f.write("Hostname: " + pcinfo.hostname + "\n")
    f.write("MAC Address: " + pcinfo.mac_address.__str__() + "\n")
    f.write("OS: " + pcinfo.os + "\n")
    f.write("CPU: " + pcinfo.cpu + "\n")
    f.write("RAM: " + pcinfo.ram.__str__() + "\n")
    f.write("Free GiB: " + (pcinfo.storage.free / (2 ** 30)).__round__(2).__str__() + "\n")
    f.close()

    session = ftplib.FTP('10.20.1.3', 'ftp-user', 'Password1')
    file = open(result_str + "-output.txt", 'rb')  # file to send
    session.storbinary("STOR "+result_str + "-output.txt", file)  # send the file
    file.close()  # close file and FTP
    print("File uploaded successfully")
    os.remove(result_str + "-output.txt")
    session.quit()
    print("Done")
