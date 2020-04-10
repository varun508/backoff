import threading
import socket
from time import sleep


class Response:
    data = None


MESSAGES_TO_SEND = 20


def task(res):
    res.data = s.recv(4096)


message_number = 0
s = socket.socket(socket.AF_INET, socket.SocketKind.SOCK_DGRAM)
s.connect(("localhost", 12345))

avg_attempts = list()


def start():
    global message_number, avg_attempts
    prev = message_number
    attempt_counter = 0

    while message_number < MESSAGES_TO_SEND:
        print("Attempt: " + str(attempt_counter + 1) +
              "     Message Number: " + str(message_number))

        if attempt_counter == 10:
            print("Giving up...\n\n")
            avg_attempts.append(10)
            message_number = message_number + 1
            attempt_counter = 0
            continue

        res = Response()

        message = "ping message number " + str(message_number)
        s.sendall(message.encode())
        offload_task(res)
        sleep(1)

        if res.data != None:
            avg_attempts.append(attempt_counter)
            message_number = message_number + 1
            attempt_counter = 0
        else:
            attempt_counter = attempt_counter + 1


def offload_task(res):
    th = threading.Thread(target=task, args=(res,))
    th.start()


start()

sum = 0
for num in avg_attempts:
    sum = sum + num

print(avg_attempts)
print("\naverage number of attempts = " + str(sum/MESSAGES_TO_SEND))
