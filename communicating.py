#imports
import logging
import time
import multiprocessing
from multiprocessing.context import Process
from multiprocessing import process
from multiprocessing.connection import Listener, Client

logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d - %(message)s', datefmt='%H:%M:%S',
                        level=logging.DEBUG)


# Worker process
def proc(server='localhost', port=6000, password=b'password123'):
    name = process.current_process().name
    logging.info(f"{name} started")

    # start listening for connections
    address = (server, port)
    listener = Listener(address, authkey=password)
    conn = listener.accept()
    logging.info(f"{name} connection from {listener.last_accepted}")

    # Loop for input from the connected process
    while True:
        msg = conn.recv()
        logging.info(f"{name} data in: {msg}")
        if msg == 'quit':
            conn.close()
            break
    listener.close()

    logging.info(f"{name} finished")


# Main functions
def main():
    name = process.current_process().name
    logging.info(f"{name} started")

    # setup the process
    address = 'localhost'
    port = 2923 # above 1024
    password = b'password123'
    p = Process(target=proc, args=[address, port, password], daemon=True, name="Worker")
    p.start()

    logging.info(f"{name} waiting on the worker ...")
    time.sleep(1)

    #  connect to the process
    dest = (address, port)
    conn = Client(dest, authkey=password)

    # command loop
    while True:
        command = input('\r\n Enter a command or type quit:\r\n').strip()
        logging.info(f"{name} command: {command}")
        conn.send(command)
        if command == 'quit':
            break
    
    # cleanup and shutdowwn
    if p.is_alive:
        logging.info(f"{name} terminating worker")
        conn.close()
        time.sleep(1)
        p.terminate()
    p.join()

    logging.info(f"{name} finished")


if __name__ == '__main__':
    main()