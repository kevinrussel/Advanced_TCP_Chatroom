import threading
import socket
import threading










def main():
    print("hello world")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1',8080))



if __name__ == "__main__":
    main()