# Thread Locking

# Imports and globals
import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random

counter = 0


# Test function
def test(count):
    global counter
    threadname = threading.current_thread().name
    logging.info(f"Starting: {threadname}")

    for x in range(count):
        logging.info(f"Count: {threadname} += {count}")

    logging.info(f"Completed: {threadname}")


# Main function
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d - %(message)s', datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging.info('App Start')

    workers = 2
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers * 2):
            v = random.randrange(1, 5)
            ex.submit(test, v)

    logging.info('App Finished')


if __name__ == "__main__":
    main()