# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:30:29 2015

@author: sharland
"""

import socket

server = 'pythonprogramming.net'

port = 80

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("pythonprogramming.net", 80))

s.send(request.encode())
result = s.recv(4096)


while (len(result) > 0):
    print(result)
    result = s.recv(4096)