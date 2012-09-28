# FILE TRANSFER SERVER

import socket, os

def sendFile(s, filename):
    if fileExist(s, filename):
        filehandle = open(filename,'r')
        file_read = filehandle.read()
        filehandle.close()
        print 'PRINTING FILE_READ: '+file_read
        msg = 'OK '+str(os.path.getsize(filename))+'\n'+file_read
        s.send(msg)

def fileExist(s, filename):
    if not os.path.exists(filename):
        s.send("ERROR %s is an invalid path" % filename)
        print("-ERROR- File Requested Does Not Exist: %s" % filename)
        return False
    else:
        return True

def main():
    datalist = []
    HOST = ''
    PORT = 9998

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    
    while True:
        conn, addr = s.accept()
        while True:
            data = conn.recv(1024)
            if not data: break
            newdata = repr(data)
            newdata = newdata.strip('\'')
            for item in newdata.split('\\n'):
                if item != ' ' and item != '':
                    datalist.append(item)
            for part in datalist:
                if part.startswith("GET"):
                    filename = part.split()[1]
                    sendFile(conn, filename)
        conn.close()

main()
