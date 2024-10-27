import socket
import re


s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
def is_valid_ip(ip): #checking for validity of IP address input
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if pattern.match(ip):
        return all(0 <= int(part) <= 255 for part in ip.split('.'))
    return False


Host=input('please enter the ip address you want to scan: ')
while not is_valid_ip(Host):
    Host= input('please enter a valid ip address: ')
print(' you have entered a valid ip address which is: ', host)
        
port=input('please enter the port number you want to scan: ')
while not port.isdigit():
        port=int('please enter a valid port number: ')
port=int(port)
print('you have entered a valid port number: ', port)



def portscanner(port):
    if s.connect_ex((host,port)):
        print('This port is closed unfortunately')
    else:
        print('This port is open')

portscanner(port)
