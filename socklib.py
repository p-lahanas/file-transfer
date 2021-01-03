import socket
import sys

from error import SOCK_ERR

def new_sock():
    """Returns a TCP internet socket."""
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sock_create_bind(host, port):
    """Returns a socket which is bound to the specified host and port."""
    sock = new_sock()
    try:
        sock.bind((host, port))
    except socket.error:
        print("Error binding socket")
        sys.exit(SOCK_ERR) 
    return sock

def sock_create_connect(host, port):
    """Returns a socket connection to the specified host and port."""
    sock = new_sock()
    try:
        sock.connect((host, port))
    except socket.error:
        print("Error connecting to host")
    return sock