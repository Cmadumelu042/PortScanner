import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

host=input('please enter the ip address you want to scan: ').isdecimal
while not host.isdecimal():
        host= input('please enter a valid ip address: ')
        print(' you have entered a valid ip address', host)
        
port=int(input('please enter the port number you want to scan: '))
while not port.isdigit():
        port=int('please enter a valid port number: ')
        print('you have entered a valid port number: ', port)



def portscanner(port):
    if s.connect_ex((host,port)):
        print('port is close')
    else:
        print('port is open')

portscanner(port)