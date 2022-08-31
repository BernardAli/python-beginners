# sudo lsof -i -P -n | grep LISTEN
# sudo lsof -i -P -n

# Imports
import logging
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d - %(message)s', datefmt='%H:%M:%S',
                        level=logging.DEBUG)

# Check one port
def check_port(ip, port, timeout):
    ret = False
    logging.debug(f"Checking {ip}:{port}")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket.setdefaulttimeout(timeout)
        s.settimeout(timeout)
        conn = s.connect_ex((ip, port))
        logging.debug(f"Connected to {ip}:{port} = {conn}")
        s.close()

        if conn == 0:
            ret = False
            logging.debug(f"In use {ip}:{port}")
        else:
            ret = True
            logging.debug(f"Usable {ip}:{port}")

    except Exception as ex:
        logging.debug(f"Error {ip}:{port} = {ex.msg}")
    finally:
        logging.debug(f"Returning {ip}:{port} = {ret}")
        return ret


# checking a range
def check_range(ip, scope):
    ret = {}
    for p in scope:
        r = check_port(ip, p, 1.0)
        ret[p] = r
    return ret


# Main Function
def main():
    # Test one port
    p = check_port("localhost", 2594, 2)
    logging.info(f"Port 2594 usable: {p}")

    # test a range of ports
    ports = check_range('localhost', range(49000, 50001))
    for k, v in ports.items():
        logging.info(f"Port {k} usable: {v}")


if __name__ == '__main__':
    main()