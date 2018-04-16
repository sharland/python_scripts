# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:26:29 2015

@author: sharland
"""
import socket

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print(s)


server = 'www.bbc.co.uk'

port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)