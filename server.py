import threading
import socket








server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LOCAL_IP_ADDRESS = '127.0.0.1'
LOCAL_PORT_ADDRESS = 8080
# This will allow the port for reconnection
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
## This creates a local server right here.
server.bind((LOCAL_IP_ADDRESS,LOCAL_PORT_ADDRESS))
## How many connections we will support.
server.listen(5)