# Multiprocessing starting and stopping
# The full life cycle

# imports 
import logging
import multiprocessing
from multiprocessing.context import Process
import time

# Worker process 
def work(msg, max):
    name = multiprocessing.current_process().name
    logging.info(f"{name} started")
    for x in range(max):
        logging.info(f"{name} {msg}")
        time.sleep(1)
    logging.info(f"{name} Finished")


# Main process 
def main():
    logging.info("Started")

    max = 20
    worker = Process(target=work, args=["Working", max], daemon=True, name="worker")
    worker.start()

    time.sleep(5)

    # if the process is running, stop it
    if worker.is_alive():
        worker.terminate()
    worker.join()
    logging.info(f"Finished: {worker.exitcode}")

    logging.info("Stopped")



logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d - %(message)s', datefmt='%H:%M:%S',
                        level=logging.DEBUG)

if __name__ == '__main__':
    main()