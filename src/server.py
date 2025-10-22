import socket
# Socket it is lika a two way endpoint that receives data and sends data


s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1234))

# here basically the server will open and listen for incoming connections
s.listen(5)

# this loop is when it is listening for connections
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    # sends information to the client socket
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
    