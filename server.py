#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os



class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion" + b"\r\n")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()

            if not line:
                break
            client_message = line.decode('utf-8').split()
            if client_message[0] == 'INVITE':
                print("El cliente nos manda " + line.decode('utf-8'))
                self.wfile.write(b"SIP/2.0 100 Trying\r\n" +
                                b"SIP/2.0 180 Ring\r\n" +
                                b"SIP/2.0 200 OK\r\n")
            elif client_message[0] == 'ACK':
                print("El cliente nos manda " + line.decode('utf-8'))
                aEjecutar = 'mp32rtp -i 127.0.0.1 -p 23032 < ' + Audio_file
                print("Vamos a ejecutar: " + aEjecutar)
                os.system(aEjecutar)

                
            # Si no hay más líneas salimos del bucle infinito


if __name__ == "__main__":
    try:
        IP = sys.argv[1]
        PORT = sys.argv[2]
        Audio_file = sys.argv[3]
    except:
        sys.exit("Usage: python server.py IP port audio_file")

    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', int(PORT)), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
