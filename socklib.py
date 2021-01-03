import socket
import sys

from error import SOCK_ERROR 

"""
Creates a new socket bound to a particular port
"""
def sock_create_bind(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
    except socket.error:
        print("Error Creating Socket\n")
        sys.exit(SOCK_ERROR) 
