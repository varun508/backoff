import random
from time import sleep
from socket import *

BUSY_PERCENT = 50
SERVER_PORT = 12345


def get_busy():
    random_number = random.randint(0, 100)
    if random_number < BUSY_PERCENT:
        print("Getting busy ...")
        sleep(1)


server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', SERVER_PORT))
print('The server is ready to receive requests')

while True:
    get_busy()
    message, client_address = server_socket.recvfrom(2048)
    print('\nReceiving message: ', message.decode(),
          '\nfrom client: ', client_address)
    modified_message = message.decode().upper()
    server_socket.sendto(modified_message.encode(), client_address)
    get_busy()
