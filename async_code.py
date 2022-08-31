# imports 
import logging
import multiprocessing
import threading
import asyncio
import random

logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d - %(message)s', datefmt='%H:%M:%S',
                        level=logging.DEBUG)

def display(msg):
    threadname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f"{processname} \ {threadname} :{msg}")


async def work(name):
    display(name + " starting")

    # Do something
    await asyncio.sleep(random.randint(0, 10))
    display(name + " finished")


async def run_async(max):
    tasks = []
    for x in range(max):
        name = "Item" + str(x)
        tasks.append(asyncio.ensure_future(work(name)))

    await asyncio.gather(*tasks)


# Main function
def main():
    display("Main Started")
    loop = asyncio.get_event_loop()

    # loop until an async task is done
    loop.run_until_complete(run_async(50))

    # will run forever!
    # loop.run_forever()

    # stop looping, free up resources
    loop.close()

    display("Main Finished")


if __name__ == "__main__":
    main()