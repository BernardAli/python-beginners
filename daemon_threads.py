# Daemon threads
# Quiting when we quit the app 


# Import
import logging
import threading
from threading import Thread, Timer
import time


# Test functions
def test():
    threadname = threading.current_thread().name
    logging.info(f"Starting: {threadname}")
    for x in range(60):
        logging.info(f"Working: {threadname}")
        time.sleep(1)
    logging.info(f"Finished: {threadname}")


def stop():
    logging.info("Exiting the application")
    exit(0)


# Main Functions
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d - %(message)s', datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging.info('Main Thread Started')

    # stop in three seconds
    timer = Timer(3, stop)
    timer.start()

    # Run the thread
    t = Thread(target=test, daemon=True)
    t.start()

    logging.info('Main Thread Finished')


if __name__ == "__main__":
    main()