#!/usr/bin/env python

import socket
import protocol_client as pc

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

def send_to_server(sckt, msg):
    sckt.sendto(msg.encode(), (TCP_IP,TCP_PORT))
    print("> Client:", msg)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

# Ask for files list
send_to_server(s, pc.START)
data = s.recv(BUFFER_SIZE)
files = data.decode()
print("< Server: This is the list of files available:")
print(files)

# Ask for specific file
send_to_server(s, pc.SEND_FILE)
filename = input("Type the filename that you desire: ")
send_to_server(s, filename)

# Receive file
data = s.recv(BUFFER_SIZE)
file_start = data.decode()
print("< Server:", file_start)
file_size = int(file_start.split(":")[1])
send_to_server(s, pc.OK)
data = s.recv(file_size)
desired_file = data.decode()
print("< Server:", desired_file)

# End connection
send_to_server(s, pc.END)
s.close()
