import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

#http://data.pr4e.org/romeo.txt

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() # Windows: \r\n\r\n because using windows, MAC & Linux \n\n
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ):
        break
    print(data.decode())
    
mysock.close()