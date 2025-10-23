import socket
from log import logger 
# Socket it is lika a two way endpoint that receives data and sends data


# msg = "Welcome to the message!"
# # creating a fixed length header
# print(f"{len(msg):<20}"+msg)

HEADER_SIZE = 10

# if ran on a webserver then bind to the ip address you can find with ipconfig and you have to connect to a public ip address
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1234))

# here basically the server will open and listen for incoming connections
s.listen(5)

# this loop is when it is listening for connections
while True:
    clientsocket, address = s.accept()
    # print(f"Connection from {address} has been established!")
    logger.info(f"Connection from {address} has been established!")
    # sends information to the client socket
    msg = "Welcome to the server!"
    # creating a fixed length header
    msg = f"{len(msg):<{HEADER_SIZE}}" + msg

    clientsocket.send(bytes(msg, "utf-8"))