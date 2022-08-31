# Imports
import logging
import multiprocessing
from multiprocessing import process
import time


# Process starting function
def run(num):
    name = process.current_process().name
    logging.info(f"Running process {name} as {__name__}")
    time.sleep(num * 8)
    logging.info(f"Process {name} finished")


# Basic process usage

def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d - %(message)s', datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    name = process.current_process().name
    logging.info(f"Running process {name} as {__name__}")

    processes = []
    for x in range(5):
        p = multiprocessing.Process(target=run, args=[x], daemon=True)
        processes.append(p)
        p.start()

    # wait for the processes
    for p in processes:
        p.join()

    logging.info(f"Finished process {name}")


if __name__ == "__main__":
    main()