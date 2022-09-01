# imports 
import logging
import socket
import select

logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d - %(message)s', datefmt='%H:%M:%S',
                        level=logging.DEBUG)

# Blocking socket example
def create_blocking(host, ip):
    logging.info("Blocking - creating socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logging.info("Blocking - connecting")
    s.connect((host, ip))

    logging.info("Blocking - connected")
    logging.info("Blocking - sending")

    s.send(b"hello\r\n")

    logging.info("Blocking - waiting ...")
    data =s.recv(1024)
    logging.info(f"Blocking - data = {len(data)}")
    logging.info("Blocking - closing ...")
    s.close()


# Non Blocking socket example
def create_nonblocking(host, ip):
    logging.info("Non Blocking - creating socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logging.info("Non Blocking - connecting")
    ret = s.connect_ex((host, ip))

    if ret != 0:
        logging.info("Non Blocking - failed to connect!")
        return
    
    logging.info("Non Blocking - connected!")
    s.setblocking(False)

    inputs = [s]
    outputs = [s]

    while inputs:
        logging.info("Non Blocking - waiting ...")
        readable, writable, exceptional = select.select(inputs, outputs, inputs, 0.5)

        for s in writable:
            logging.info("Non Blocking - sending!")
            data = s.send(b"hello\r\n")
            logging.info(f"Non Blocking - sent = {data}")
            outputs.remove(s)

        for s in readable:
            logging.info("Non Blocking - sending!")
            data = s.recv(1024)
            logging.info(f"Non Blocking - data = {len(data)}")
            logging.info(f"Non Blocking - closing")
            s.close()
            inputs.remove(s)
            break

        for s in exceptional:
            logging.info("Non Blocking - error!")
            outputs.remove(s)
            inputs.remove(s)
            break


# Main function
def main():
    # create_blocking("voidrealms.com", 80)
    create_nonblocking("voidrealms.com", 80)

if __name__ == '__main__':
    main()