# FILE TRANSFER CLIENT

import socket

def main():
    filename = raw_input("What file would you like to request? ")
    HOST = 'localhost'
    PORT = 9998
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    s.send('GET %s\n'%filename)
    data = s.recv(1024)
    s.close()
    handle = open('boff_ftp_success!.txt', 'w')
    handle.write(data.split(' ',2)[2])
    handle.close()

main()
