# Imports
import logging
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d - %(message)s', datefmt='%H:%M:%S',
                        level=logging.DEBUG)

# TCP Server
def server(ip, port):
    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip, port)

    logging.info(f'Bind: {ip}: {port}')
    s.bind(address)

    logging.info('Listening')
    s.listen(1)


    conn, addr = s.accept()
    logging.info(f"Connected: {addr}")

    while True:
        data = conn.recv(1024)
        if len(data) == 0:
            logging.info(f"Exiting")
            conn.close()
            break
        logging.info(f"Data: {data}")
    
    logging.info("Closing the Server")
    s.close()


# Main Function
def main():
    server("localhost", 2607)


if __name__ == "__main__":
    main()