"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging


# Basic logging
def test():
    print('-'*20)
    level = logging.getLevelName(logging.getLogger().getEffectiveLevel())
    print(f'Log level: {level}')
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.error('error message')
    logging.critical('critical message')
    print('-'*20)

test()


# Loggin levels
# Getting and setting logging levels
# Allows for the filtering 

# Get the root logger
rootlog = logging.getLogger()
print(f'Level: {logging.getLevelName(rootlog.getEffectiveLevel())}')


# Set it to debug
rootlog.setLevel(logging.DEBUG)
test()


# Set it to critical
rootlog.setLevel(logging.CRITICAL)
test()


# Set it to warning
rootlog.setLevel(logging.WARNING)
test()


# Log to file 
handler = logging.FileHandler('file.log')

formatter = logging.Formatter()