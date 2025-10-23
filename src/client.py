import socket
from log import logger

HEADER_SIZE = 10

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# the client contrary to the server, instead of binding it just straight up connects

s.connect((socket.gethostname(), 1234))

# accept the message

# you can buffer data meaning that you can send it in small packages instead

while True:

    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        # print(decoded_message)
        if new_msg:
            logger.info(f"New message length: {msg[:HEADER_SIZE]}")
            msglen = int(msg[:HEADER_SIZE])
            new_msg = False

        full_msg += msg.decode("utf-8")
        if len(full_msg) - HEADER_SIZE == msglen:
            logger.info("Full message rcvd")
            logger.info(full_msg[HEADER_SIZE:])
            new_msg = True
            full_msg = ''
    print(full_msg)
    
