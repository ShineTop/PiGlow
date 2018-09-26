#!/usr/bin/python3
"""
Jewels in the Cave

This program randomly turns on an LED, and then randomly turns one
on and off. At a brightness setting of 1, the LEDs look like jewels.

List of jewels:
    Red = Ruby
    Orange = Citrine
    Yellow = Beryl
    Green = Emerald
    Blue = Sapphire
    White = Diamond

....................

Functions:
- jewels_in_the_cave: Randomly turns on and off an LED

....................

Requirements:
    PyGlow.py (many thanks to benleb for this program)
    print_piglow_header.py

You will have these files if you downloaded the entire repository.

....................

Author: Paul Ryan

This program was written on a Raspberry Pi using the Geany IDE.
"""
########################################################################
#                          Import modules                              #
########################################################################

import os
import logging
import random
from time import sleep
from PyGlow import PyGlow
from print_piglow_header import print_piglow_header

########################################################################
#                           Initialize                                 #
########################################################################

PYGLOW = PyGlow()
PYGLOW.all(0)

SLEEP_SPEED = 0.10

# Logging
LOG = 'jewels_in_the_cave.log'
LOG_FORMAT = '%(asctime)s %(name)s: %(funcName)s: %(levelname)s: %(message)s'
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.ERROR)    # Nothing will log unless changed to DEBUG
FORMATTER = logging.Formatter(fmt=LOG_FORMAT,
                              datefmt='%m/%d/%y %I:%M:%S %p:')
FILE_HANDLER = logging.FileHandler(LOG, 'w')
FILE_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(FILE_HANDLER)

########################################################################
#                            Functions                                 #
########################################################################


def main():
    """ The main fuction """

    print_piglow_header()

    # Force white text after selecting random colored header
    print("\033[1;37;40mPress Ctrl-C to stop the program.")
    try:
        while True:
            jewels_in_the_cave()
    # Stop the program and turn off LEDs with Ctrl-C
    except KeyboardInterrupt:
        stop()


def jewels_in_the_cave():
    """
    Randomly turns on and off an LED
    """

    sleep_speed = 0.5
    brightness = 1
    list_of_leds = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                    10, 11, 12, 13, 14, 15, 16, 17, 18]

    sleep(sleep_speed)
    # Turn on a random led
    random_led = int(random.choice(list_of_leds))
    PYGLOW.led(random_led, brightness)
    sleep(sleep_speed)
    # Turn off a random led
    random_led = int(random.choice(list_of_leds))
    PYGLOW.led(random_led, 0)
    sleep(sleep_speed)


def delete_empty_logs():
    """
    Delete empty log fles

    Log files will always be created. But they will be empty if the
    log level is set to anything higher than DEBUG, since only DEBUG
    messages are logged. If the log files are empty, they will be
    deleted.
    """

    logs = [LOG, 'print_piglow_header.log']

    for log in logs:
        if os.stat(log).st_size == 0:
            os.remove(log)


def stop():
    """
    Print exit message and turn off the PiGlow
    """
    LOGGER.debug("END")
    delete_empty_logs()
    print("\nExiting program.")
    PYGLOW.all(0)


if __name__ == '__main__':
    main()
