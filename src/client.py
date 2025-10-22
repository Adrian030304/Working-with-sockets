import socket
from log import logger

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# the client contrary to the server, instead of binding it just straight up connects

s.connect((socket.gethostname(), 1234))

# accept the message

# you can buffer data meaning that you can send it in small packages instead
while True:
    msg = s.recv(8)
    decoded_message = msg.decode("utf-8")
    # print(decoded_message)
    if len(msg) <= 0:
        break
    logger.info(decoded_message)
    
