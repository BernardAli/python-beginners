# TCP Client
# Intro to networking concepts

# Imports
import logging
import socket


logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d - %(message)s', datefmt='%H:%M:%S',
                        level=logging.DEBUG)

# TCP Client
def downlaod(server, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (server, port)
    logging.info(f"Connecting to: {server}:{port}")

    s.connect(address)
    logging.info(f"Connected")

    logging.info("Send")
    s.send(b"Hello\r\n")

    logging.info("Recv")
    data = s.recv(1024)

    logging.info("Closing")
    s.close()

    logging.info(f"Data {data}")


# Main Function
def main():
    downlaod("youtube.com", 80)



if __name__ == "__main__":
    main()