# Imports
import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from queue import Queue


# Queues
# Use Queue to pass messages back and forth

def test_queue(name, que):
    threadname = threading.current_thread().name
    logging.info(f"Starting: {threadname}")
    time.sleep(random.randrange(1, 5))
    logging.info(f"Finished: {threadname}")
    ret = f"Hello {name}, your random number is {str(random.randrange(1, 50))}"
    que.put(ret)

def queued():
    que = Queue()   
    t = Thread(target=test_queue, args=["Ben", que])
    t.start()
    logging.info("Do someting on the main thread")
    t.join()
    ret = que.get()
    logging.info(f"Returned: {ret}")


# Futures
# Use futures, easier and cleaner
def test_future(name):
    threadname = threading.current_thread().name
    logging.info(f"Starting: {threadname}")
    time.sleep(random.randrange(1, 5))
    logging.info(f"Finished: {threadname}")
    ret = f"Hello {name}, your random number is {str(random.randrange(1, 50))}"
    return ret

def pooled():
    workers = 20
    ret = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers):
            v = random.randrange(1, 5)
            future = ex.submit(test_future, "Ben" + str(x))
            ret.append(future)
    logging.info("Do someting on the main thread")
    for r in ret:
        logging.info(f"Returned: {r.result()}")

# Main
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d - %(message)s', datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging.info('App Start')
    # queued()
    pooled()


if __name__ == "__main__":
    main()