#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.

try:
    Method = sys.argv[1]
    Receiver = sys.argv[2]
except:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")

Receiver_ID = Receiver.split('@')
Login = Receiver.split('@')[0]
SERVER = Receiver_ID[1].split(":")[0]
PORT = int(Receiver_ID[1].split(":")[1])


# Contenido que vamos a enviar
LINE = Method + ' sip:' + Receiver.split(':')[0] + ' SIP/2.0'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')

try:
    data = my_socket.recv(1024)
except ConnectionRefusedError:
    sys.exit(" Connection Refused ERROR ")

print('Recibido -- ', data.decode('utf-8'))
DataList = data.decode('utf-8').split()

if DataList[2] == 'Trying' and DataList[5] == 'Ring' and DataList[8] == 'OK':
    M_ACK = 'ACK sip:' + Receiver.split(':')[0] + ' SIP/2.0'
    my_socket.send(bytes(M_ACK, 'utf-8') + b'\r\n')
    print("Enviando: " + M_ACK)
    data = my_socket.recv(1024)

print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
