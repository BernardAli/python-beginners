# Timers
# Execute code at timed intervals
# This is the first step in learning threading

import time
from threading import Timer


def display(msg):
    print(f"{msg} {time.strftime('%H:%M:%S')}")


# Basic timer
def run_once():
    display('Run once:')
    t = Timer(5, display, ['Timeout: '])
    t.start()


run_once()

# Notice this runs immediately and once
print("waiting ...")


# Interval timer
# Wrap it into a class
# Make it run until we stop it

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
        print('Done')


# Really we are making a thread abd controlling it
timer = RepeatTimer(1, display, ['Repeating'])
timer.start()
print('thread started')
time.sleep(10)  # suspends execution for the given number of seconds
print('threading finishing')

timer.cancel()